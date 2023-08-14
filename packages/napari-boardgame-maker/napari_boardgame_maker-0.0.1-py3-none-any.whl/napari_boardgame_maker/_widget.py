"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from qtpy.QtWidgets import QWidget, QFileDialog
from qtpy import uic
from qtpy.QtCore import QEvent, QObject

from matplotlib.patches import CirclePolygon, Circle
from skimage.draw import polygon2mask
from scipy.ndimage import distance_transform_edt
from scipy import spatial, optimize
import vedo
import copy

from magicgui.widgets import create_widget

from pathlib import Path
import os
import numpy as np
import napari
from napari_tools_menu import register_function

@register_function(menu="Games > Boardgame tile maker (npbgm)")
class BoardgameMakerWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        uic.loadUi(Path(os.path.dirname(__file__)) / "tile_maker.ui", self)

        # add widget select at top of gridlayout
        self.image_layer_select = create_widget(annotation=napari.layers.Image, label="Image_layer")
        self.layout().addWidget(self.image_layer_select.native, 0, 1, 1, 3)
        
        self.pushButton_make_outline.clicked.connect(self._create_outline)
        self.pushButton_run.clicked.connect(self._create_tile)
        self.pushButton_create_number_field.clicked.connect(self._create_number_field)

        self.spinBox_hexagon_radius.valueChanged.connect(self._create_outline)
        self.spinBox_number_field_radius.valueChanged.connect(self._create_number_field)

        # Connect pixel/mm converters
        self.spinBox_number_field_radius_mm.valueChanged.connect(self._update_pixel_values)
        self.spinBox_stride_mm.valueChanged.connect(self._update_pixel_values)
        self.spinBox_slope_width_mm.valueChanged.connect(self._update_pixel_values)
        self.spinBox_townradius_mm.valueChanged.connect(self._update_pixel_values)
        
        self.spinBox_number_field_radius.valueChanged.connect(self._update_mm_values)
        self.spinBox_stride.valueChanged.connect(self._update_mm_values)
        self.spinBox_slope_width.valueChanged.connect(self._update_mm_values)
        self.spinBox_townradius.valueChanged.connect(self._update_mm_values)

        # Connect final size
        self.doubleSpinBox_final_size_mm.valueChanged.connect(self._update_pixel_values)
        self.spinBox_hexagon_radius.valueChanged.connect(self._update_pixel_values)

        # Connect save button
        self.pushButton_export.clicked.connect(self._export)

        self.center = [0, 0]
        self.outline_layer = None
        self.number_field_layer = None
        self.tile_labels_layer = None
        self.surface_final_layer = None

        self._update_pixel_values()
        self.installEventFilter(self)
    
    def eventFilter(self, obj: QObject, event: QEvent):
        if event.type() == QEvent.ParentChange:
            self.image_layer_select.parent_changed.emit(self.parent())

        return super().eventFilter(obj, event)

    def _create_outline(self):
        """Create outline of tile hexagon"""

        if self.outline_layer not in self.viewer.layers:
            self.outline_layer = None

        if self.outline_layer is None:
            self.center = np.asarray(self.image_layer_select.value.data.shape) / 2

        else:
            self.center = self.outline_layer.data[0][1:].mean(axis=0)

        self.hexagon = CirclePolygon(
            xy = (self.center[0], self.center[1]),
            radius=self.spinBox_hexagon_radius.value(),
            resolution=6)

        # add outline layer or update data
        vertices = self.hexagon.get_verts()
        if self.outline_layer is None or self.outline_layer not in self.viewer.layers:
            self.outline_layer = self.viewer.add_shapes(vertices, shape_type='polygon', name='Tile outline',
                                                        opacity=0.4, edge_width=2, edge_color='cyan')
        else:
            self.outline_layer.data = vertices

    def _create_number_field(self):
        """Create number field around center of tile"""

        if self.number_field_layer not in self.viewer.layers:
            self.number_field_layer = None

        if self.number_field_layer is not None:
            center = self.number_field_layer.data[0][1:].mean(axis=0)
        else:
            center = self.center

        # Add number valley by indending mask in a circle around a given center
        circle_number = Circle(radius=self.spinBox_number_field_radius.value(), xy=center)
        vertices_circle_number_field = circle_number.get_verts()

        if self.number_field_layer is None:
            self.number_field_layer = self.viewer.add_shapes(
                vertices_circle_number_field, shape_type='polygon',
                name='Number field', opacity=0.4, edge_width=2, edge_color='orange')
        else:
            self.number_field_layer.data = vertices_circle_number_field

    def _calculate_conversion_factor(self):
        """Calculate conversion factor between mm and pixel values"""
        radius_in_px = self.spinBox_hexagon_radius.value()
        radius_in_mm = self.doubleSpinBox_final_size_mm.value() / 2
        self.conversion_factor = radius_in_mm / radius_in_px

    def _update_pixel_values(self):
        """Update pixel values based on mm values"""
        self._calculate_conversion_factor()

        # block signals to avoid infinite loop
        to_update = [self.spinBox_stride,
                     self.spinBox_slope_width,
                     self.spinBox_townradius,
                     self.spinBox_number_field_radius]
        [x.blockSignals(True) for x in to_update]

        self.spinBox_stride.setValue(int(self.spinBox_stride_mm.value() / self.conversion_factor))
        self.spinBox_slope_width.setValue(int(self.spinBox_slope_width_mm.value() / self.conversion_factor))
        self.spinBox_townradius.setValue(int(self.spinBox_townradius_mm.value() / self.conversion_factor))
        self.spinBox_number_field_radius.setValue(int(self.spinBox_number_field_radius_mm.value() / self.conversion_factor))
        [x.blockSignals(False) for x in to_update]

    def _update_mm_values(self):
        """Update mm values based on pixel values"""
        self._calculate_conversion_factor()

        # block signals to avoid infinite loop
        to_update = [self.spinBox_stride_mm,
                     self.spinBox_slope_width_mm,
                     self.spinBox_townradius_mm,
                     self.spinBox_number_field_radius_mm]
        [x.blockSignals(True) for x in to_update]

        self.spinBox_stride_mm.setValue(int(self.spinBox_stride.value() * self.conversion_factor))
        self.spinBox_slope_width_mm.setValue(int(self.spinBox_slope_width.value() * self.conversion_factor))
        self.spinBox_townradius_mm.setValue(int(self.spinBox_townradius.value() * self.conversion_factor))
        self.spinBox_number_field_radius_mm.setValue(int(self.spinBox_number_field_radius.value() * self.conversion_factor))
        [x.blockSignals(False) for x in to_update]
            

    def _create_tile(self):
        """Create tile mask"""
        stride = self.spinBox_stride.value()
        radius = self.spinBox_hexagon_radius.value()
        town_radius = self.spinBox_townradius.value()
        slope_width = self.spinBox_slope_width.value()
        z_multiplier = self.doubleSpinBox_z_multiplier.value()
        height_offset = self.spinBox_height_offset.value()

        # find new vertices
        self.center = np.asarray(self.outline_layer.data)[0][1:].mean(axis=0)
        vertices_outer = self.hexagon.get_path().vertices * radius + self.center[None,:]
        vertices_inner = self.hexagon.get_path().vertices * (radius - stride) + self.center[None,:]

        # convert inner and outer hexagon to mask
        image = self.image_layer_select.value.data
        tile_mask = polygon2mask(image.shape, vertices_outer) * 1
        tile_mask += polygon2mask(image.shape, vertices_inner) * 1

        for vertex in vertices_outer:
            town_area = Circle(xy=vertex, radius=town_radius)
            vertices_town = town_area.get_path().vertices * town_radius + vertex[None, :]
            town_mask = polygon2mask(image.shape, vertices_town) * (tile_mask != 0)
            tile_mask[town_mask == 1] = 1

        if self.tile_labels_layer not in self.viewer.layers or self.tile_labels_layer is None:
            self.tile_labels_layer = self.viewer.add_labels(tile_mask, name='Tile labels')
        else:
            self.tile_labels_layer.data = tile_mask

        # Make smooth transition with a sigmoidal function
        edt = distance_transform_edt(tile_mask==2)

        def sigmoid(x, k, x0=slope_width/2):
            y = 1 / (1 + np.exp(-k*(x-x0)))
            return y

        def error_function_1(k):
            return sigmoid(0, k) - 0.01
        
        k_val = optimize.newton(error_function_1, 0.1)
        edt_sigmoid = sigmoid(edt, k_val, slope_width/2)

        image = (image - image[tile_mask >= 1].min()) * z_multiplier
        image = image * edt_sigmoid
        image[tile_mask == 0] = 0
        image[tile_mask >= 1] += height_offset 

        mask_number_field = polygon2mask(image.shape, self.number_field_layer.data[0])
        local_minimum = image[mask_number_field == True].min()
        image[mask_number_field] = local_minimum

        # Convert to mesh
        coordinates = np.argwhere(image > 0)
        z_values = []
        for coord in coordinates:
            z_values.append(image[coord[0], coord[1]])

        tri = spatial.Delaunay(coordinates)
        points_mesh = np.zeros((coordinates.shape[0], 3))
        points_mesh[:, 1:] = coordinates
        points_mesh[:, 0] =  z_values
        surface = (points_mesh, tri.simplices)

        # need to swap axis because vedo has different convention
        points = copy.deepcopy(surface[0])
        points[:, 0] = surface[0][:, 2]
        points[:, 2] = surface[0][:, 0]

        # Extrude
        vedo_mesh = vedo.Mesh((points, surface[1]))
        n_vertices = vedo_mesh.N()

        vedo_mesh_extruded = vedo_mesh.extrude(zshift=-10)
        surface_extrude = (vedo_mesh_extruded.points(), np.asarray(vedo_mesh_extruded.faces()))
        deepest_point = surface_extrude[0].min(axis=0)[-1]
        surface_extrude[0][n_vertices:, 2] =  deepest_point

        # Swap back
        surface_final = copy.deepcopy(surface_extrude)
        surface_final[0][:, 0] = - surface_extrude[0][:, 2]
        surface_final[0][:, 2] = surface_extrude[0][:, 0]

        if self.surface_final_layer not in self.viewer.layers or self.surface_final_layer is None:
            self.surface_final_layer = self.viewer.add_surface(surface_final)
        else:
            self.surface_final_layer.data = surface_final

    def _export(self):
        """Export final surface as PLY"""

        if self.surface_final_layer is None:
            return
        
        # Get filename
        filename = QFileDialog.getSaveFileName(self, 'Save file', '', 'STl (*.stl)')[0]
        if filename == '':
            return
        
        surface_final = self.surface_final_layer.data
        mesh_final = vedo.mesh.Mesh((surface_final[0] * self.conversion_factor, surface_final[1]))
        mesh_final.write(filename)

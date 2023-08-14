import numpy as np


def test_widget(make_napari_viewer):

    from .._sample_data import rhone_glacier
    from .. import BoardgameMakerWidget

    image = rhone_glacier()[0][0]
    viewer = make_napari_viewer()

    # add the image
    layer = viewer.add_image(image, name='rhone')

    widget = BoardgameMakerWidget(viewer)
    viewer.window.add_dock_widget(widget, area='right')
    #widget.image_layer_select.set_choice(layer)
    widget._create_outline()
    widget._create_number_field()

    widget._create_tile()
    
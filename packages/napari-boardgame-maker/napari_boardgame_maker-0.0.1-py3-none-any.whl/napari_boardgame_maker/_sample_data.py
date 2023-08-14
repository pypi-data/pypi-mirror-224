

def rhone_glacier() -> "napari.types.LayerDataTuple":

    from skimage import io
    from pathlib import Path
    import os

    # get path to current file
    path = Path(__file__).parent

    glacier = io.imread(os.path.join(path, "sample_data", "output_NASADEM.tif"))
    glacier = (glacier, {"name": "Rhone Glacier", "colormap": "gray"}, 'image')

    print(' NASA JPL. NASADEM Merged DEM Global 1 arc second V001. 2020, distributed by NASA EOSDIS Land Processes DAAC, https://doi.org/10.5067/MEaSUREs/NASADEM/NASADEM_HGT.001.')
    return [glacier]

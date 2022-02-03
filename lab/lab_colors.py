import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time

import src.colors.palette_utils as palette_utils
from src.colors.raster import Raster


def load_image_from_file(path):
    k = 16
    img = Image.open(path)
    print("Loaded image", path)
    print("Dimensions:", img.size)

    start = time.time()
    raster = Raster(np.array(img))
    palette = palette_utils.analyze_palette(raster)
    print("Palette:", len(palette.colors), "different colors")
    k_palette = palette_utils.compress_palette(palette, k)
    print("Compressed palette to", k, "colors")
    palette_utils.apply_palette(raster, k_palette)
    print("Converted image to use compressed palette")
    bitmap = palette_utils.extract_bitmap(raster)

    end = time.time()
    print("Elapsed time:", end - start, "seconds")

    return bitmap


if __name__ == '__main__':
    # image = load_image_from_file("./resources/images/input/grumpy_dwarf.jpg")
    image = load_image_from_file("./resources/images/input/eevee_20200821.jpg")
    fig, ax = plt.subplots()
    ax.imshow(image)
    plt.show()

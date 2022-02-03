import numpy as np

import src.kmeans.kmeans as kmeans
from src.colors.palette import Color
from src.colors.palette import Palette
from src.colors.raster import Raster


def ravel_rgb_array(coordinates: np.ndarray) -> np.ndarray:
    coords = coordinates.astype(int)
    return coords[:, 0] * (2**16) + coords[:, 1] * (2**8) + coords[:, 2]


def unravel_rgb_array(values: np.ndarray) -> np.ndarray:
    r = np.bitwise_and(np.right_shift(values, 16), 255)
    g = np.bitwise_and(np.right_shift(values, 8), 255)
    b = np.bitwise_and(values, 255)
    return np.array([r, g, b]).T


def analyze_palette(image: Raster) -> Palette:
    num_points = image.bitmap.shape[0] * image.bitmap.shape[1]
    num_coords = image.bitmap.shape[2]
    colors = np.reshape(image.bitmap, (num_points, num_coords))
    values = ravel_rgb_array(colors)
    unique_values = np.unique(values)
    unique_colors = unravel_rgb_array(unique_values)
    return Palette(list(map(lambda x: Color(x), unique_colors)))


def apply_palette(image: Raster, palette: Palette):
    w = image.bitmap.shape[0]
    h = image.bitmap.shape[1]
    num_coords = image.bitmap.shape[2]
    colors = np.reshape(image.bitmap, (w * h, num_coords))
    values = ravel_rgb_array(colors)
    coded_values = np.vectorize(palette.values_to_indices.__getitem__)(values)
    image.bitmap = np.reshape(coded_values, (w, h))
    image.palette = palette


def compress_palette(palette: Palette, to_num_colors: int) -> Palette:

    def round_center(cluster) -> Color:
        return Color(np.round(cluster.center.coordinates).astype(int))

    clusters = kmeans.run(palette.colors, to_num_colors)
    k_palette = Palette(list(map(round_center, clusters)))
    for c in clusters:
        k_palette.add_equivalents(round_center(c), c.points)
    return k_palette


def extract_bitmap(image: Raster) -> np.ndarray:
    if not image.palette:
        return image.bitmap
    w = image.bitmap.shape[0]
    h = image.bitmap.shape[1]
    num_coords = image.palette.colors[0].coordinates.shape[0]
    indexed_colors = np.reshape(image.bitmap, w * h)
    coded_colors = np.vectorize(image.palette.get_coded_value)(indexed_colors)
    decoded_colors = unravel_rgb_array(coded_colors)
    bitmap = np.reshape(decoded_colors, (w, h, num_coords))
    return bitmap

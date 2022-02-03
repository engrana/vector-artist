from unittest import TestCase
import numpy as np

from src.colors.color import Color
import src.colors.palette_utils as palette_utils
from src.colors.palette import Palette
from src.colors.raster import Raster


def get_n_colors(n):
    orig_colors = []
    for i in range(n):
        orig_colors.append(Color([i + 1, i + n / 2 + 1, i + n + 2]))
    return orig_colors


class TestPaletteUtils(TestCase):

    def test_ravel_rgb_color(self):
        """ Test encoding of a RGB color to number """
        colors = np.array([108, 0, 255, 128, 75, 159]).reshape(2, 3)
        result = palette_utils.ravel_rgb_array(colors)
        self.assertTrue(np.array_equal(np.array([7078143, 8407967]), result))

    def test_unravel_rgb_color(self):
        """ Test decoding of a number to RGB color"""
        values = np.array([7078143, 8407967])
        result = palette_utils.unravel_rgb_array(values)
        self.assertTrue(np.array_equal(np.array([108, 0, 255, 128, 75, 159]).reshape(2, 3), result))

    def test_compress_palette(self):
        """ Test compressing a palette of colors """
        n = 100
        k = 8
        orig_palette = Palette(get_n_colors(n))
        result = palette_utils.compress_palette(orig_palette, k)
        self.assertEqual(k, len(result.colors))
        self.assertEqual(k, len(result.coded_values))
        self.assertTrue(len(result.values_to_indices) >= n)

    def test_extract_bitmap(self):
        """ Test converting a raster to bitmap representation """
        n = 100
        colors = get_n_colors(n)
        palette = Palette(colors)
        indexed_bitmap = np.array([range(n), range(n), range(n)]).reshape(20, 15)
        raster = Raster(indexed_bitmap, palette)
        result = palette_utils.extract_bitmap(raster)
        self.assertEqual((20, 15, 3), result.shape)
        self.assertEqual(int, result.dtype)

    def test_compress_image(self):
        """ Test image compression by color palette reduction """
        colors = list(map(lambda x: x.coordinates, get_n_colors(100)))
        input_bitmap = np.array(colors).astype(int).reshape((10, 10, 3))
        raster = Raster(input_bitmap)
        orig_palette = palette_utils.analyze_palette(raster)
        compressed_palette = palette_utils.compress_palette(orig_palette, 8)
        palette_utils.apply_palette(raster, compressed_palette)
        output_bitmap = palette_utils.extract_bitmap(raster)
        self.assertEqual(np.shape(input_bitmap), np.shape(output_bitmap))

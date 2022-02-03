import numpy as np

from src.colors.color import Color
import src.colors.palette_utils as palette_utils


class Palette:

    def __init__(self, colors: [Color]):
        self.colors = colors
        coordinates = np.array(list(map(lambda c: c.coordinates, colors)))
        self.coded_values = palette_utils.ravel_rgb_array(coordinates)
        self.values_to_indices = dict(zip(self.coded_values, np.arange(len(colors), dtype=int)))

    def get_coded_value(self, index: int) -> int:
        return self.coded_values[index]

    def add_equivalents(self, representative: Color, equivalents: [Color]):
        coordinates = np.array(list(map(lambda c: c.coordinates, equivalents)))
        new_coded_values = palette_utils.ravel_rgb_array(coordinates)
        representative_value = palette_utils.ravel_rgb_array(np.array([representative.coordinates]))[0]
        representative_index = np.where(self.coded_values == representative_value)
        assert len(representative_index) == 1
        new_mappings = dict(zip(new_coded_values, representative_index[0] * np.ones(len(new_coded_values), dtype=int)))
        self.values_to_indices.update(new_mappings)

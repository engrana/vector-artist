from src.colors.palette import Palette


class Raster:
    def __init__(self, bitmap, palette: Palette = None):
        self.bitmap = bitmap
        self.palette = palette

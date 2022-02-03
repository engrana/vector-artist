import numpy as np


class Point:
    def __init__(self, coordinates):
        if isinstance(coordinates, np.ndarray):
            self.coordinates = coordinates
        else:
            self.coordinates = np.array(coordinates)

    def __add__(self, other):
        return Point(self.coordinates + other.coordinates)

    def __sub__(self, other):
        return Point(self.coordinates - other.coordinates)

    def __truediv__(self, n: int):
        return Point(self.coordinates / n)

    def __eq__(self, other) -> bool:
        return np.array_equal(self.coordinates, other.coordinates)

    def __hash__(self):
        return hash(str(self.coordinates))

    def __str__(self) -> str:
        return str(self.coordinates)

    def __repr__(self):
        return repr(self.coordinates)

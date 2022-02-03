from src.kmeans.point import Point


class Cluster:
    def __init__(self, center: Point, points=None):
        if points is None:
            points = []
        self.center = center
        self.points = points

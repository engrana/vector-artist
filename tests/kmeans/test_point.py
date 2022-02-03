from unittest import TestCase
from src.kmeans.point import Point


class TestPoints(TestCase):
    def test_point_add_point(self):
        """ Test the sum of 2 points """
        p1 = Point([1, 5, 200])
        p2 = Point([2, 4, 55])
        result = p1 + p2
        self.assertEqual(Point([3, 9, 255]), result)

    def test_point_subtract_point(self):
        """ Test the subtraction of 2 points """
        p1 = Point([1, 5, 200])
        p2 = Point([2, 4, 55])
        result = p1 - p2
        self.assertEqual(Point([-1, 1, 145]), result)

    def test_point_divide_by_num(self):
        """ Test divide a point by a number """
        p1 = Point([16, 8, 4])
        result = p1 / 4
        self.assertEqual(Point([4, 2, 1]), result)

import random
from unittest import TestCase
from src.kmeans.point import Point
from src.kmeans.cluster import Cluster
import src.kmeans.kmeans as kmeans


def create_n_points(n):
    points = []
    for i in range(n):
        points.append(Point([i, i + 1, i + 2]))
    return points


def create_n_random_points(n):
    points = []
    for i in range(n):
        points.append(Point([
            random.randint(-1024, 1024),
            random.randint(-1024, 1024),
            random.randint(-1024, 1024)]))
    return points


class TestKMeans(TestCase):
    def test_cluster_center(self):
        """ Test center of a set of points """
        p1 = Point([2, 8, 16])
        p2 = Point([1, 5, -25])
        p3 = Point([-1, 16, 0])
        result = kmeans.center([p1, p2, p3])
        self.assertEqual(Point([2 / 3, 29 / 3, -3]), result)

    def test_random_init(self):
        """ Test random initialization of clusters """
        k = 3
        points = [Point([1, 2, 3]), Point([4, 5, 6]), Point([7, 8, 9]), Point([10, 11, 12]), Point([13, 14, 15])]
        result = kmeans.random_init(points, k)
        self.assertEqual(k, len(result))
        centers = list(map(lambda c: c.center, result))
        self.assertEqual(k, len(set(centers)))
        for center in centers:
            self.assertTrue(center)
            self.assertIn(center, points)

    def test_assign_nearest(self):
        points = create_n_points(100)
        clusters = kmeans.random_init(points, 8)
        kmeans.assign_nearest(points, clusters)
        total_assigned = sum(list(map(lambda c: len(c.points), clusters)))
        self.assertEqual(100, total_assigned)

    def test_update_centers(self):
        points = create_n_points(90)
        c1 = Cluster(Point([1, 1, 1]), points[0:30])
        c2 = Cluster(Point([2, 2, 2]), points[30:60])
        c3 = Cluster(Point([3, 3, 3]), points[60:90])
        changed = kmeans.update_centers([c1, c2, c3])
        self.assertTrue(changed)
        self.assertEqual(Point([14.5, 15.5, 16.5]), c1.center)
        self.assertEqual(Point([44.5, 45.5, 46.5]), c2.center)
        self.assertEqual(Point([74.5, 75.5, 76.5]), c3.center)
        changed = kmeans.update_centers([c1, c2, c3])
        self.assertTrue(not changed)

    def test_run_kmeans(self):
        k = 8
        points = create_n_random_points(100)
        result = kmeans.run(points, k)
        self.assertEqual(k, len(result))
        total_assigned = sum(list(map(lambda c: len(c.points), result)))
        self.assertEqual(100, total_assigned)


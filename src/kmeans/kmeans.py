from functools import reduce
import numpy as np

from src.kmeans.point import Point
from src.kmeans.cluster import Cluster


def center(points: [Point]) -> Point:
    return reduce(lambda x, y: x + y, points) / len(points)


def random_init(points: [Point], k: int) -> [Cluster]:
    points_coords = np.array(list(map(lambda p: p.coordinates, points)))
    unique_points = np.unique(points_coords, axis=0)
    random_points = unique_points[np.random.choice(len(unique_points), size=k, replace=False)]
    return list(map(lambda p: Cluster(Point(p)), random_points))


def euclidean(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.linalg.norm(a[:, np.newaxis] - b, axis=2)


def group_by_values(values):
    indices = np.arange(len(values))
    values_with_idx = np.array([values, indices]).T
    values_sorted = values_with_idx[values_with_idx[:, 0].argsort()]
    return np.split(values_sorted[:, 1], np.unique(values_sorted[:, 0], return_index=True)[1][1:])


def assign_nearest(points: [Point], clusters: [Cluster]):
    points_coords = np.array(list(map(lambda p: p.coordinates, points)))
    clusters_coords = np.array(list(map(lambda c: c.center.coordinates, clusters)))
    distances = euclidean(points_coords, clusters_coords)
    assignments = np.argmin(distances, axis=1)
    points_idx_by_cluster = group_by_values(assignments)

    for i in range(len(clusters)):
        assigned_points = list(map(lambda idx: points[idx], points_idx_by_cluster[i]))
        clusters[i].points = assigned_points


def update_centers(clusters: [Cluster]) -> bool:
    changed = False
    for c in clusters:
        new_center = center(c.points)
        if new_center != c.center:
            c.center = new_center
            changed = True
    return changed


def run(points: [Point], k: int) -> [Cluster]:
    clusters = random_init(points, k)
    converged = False
    while not converged:
        assign_nearest(points, clusters)
        converged = not update_centers(clusters)
    return clusters

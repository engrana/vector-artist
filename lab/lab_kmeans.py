import random
import time

from src.kmeans.point import Point
import src.kmeans.kmeans as kmeans


def create_n_random_points(n):
    points = []
    for i in range(n):
        points.append(Point([
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)]))
    return points


def run_kmeans_with(k, n):
    points = create_n_random_points(n)
    start = time.time()
    c = kmeans.run(points, k)
    end = time.time()
    print("Elapsed time:", end - start, "seconds")
    return c


if __name__ == '__main__':
    clusters = run_kmeans_with(16, 100000)

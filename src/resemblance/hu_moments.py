import numpy as np
import cv2 as cv


def hu_moments(img: np.ndarray) -> np.ndarray:
    grayscale = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    _, thresholds = cv.threshold(grayscale, thresh=127, maxval=255, type=cv.THRESH_BINARY)
    moments = cv.moments(thresholds, binaryImage=True)
    hu_m = cv.HuMoments(moments).flatten()
    return hu_m


def normalize(hu_m: np.ndarray) -> np.ndarray:
    return np.copysign(1.0, hu_m) * np.log10(abs(hu_m))


def compare(img1: np.ndarray, img2: np.ndarray) -> float:
    hum1 = normalize(hu_moments(img1))
    hum2 = normalize(hu_moments(img2))
    square_diff = abs(hum1 - hum2) ** 2
    return np.sum(-square_diff)

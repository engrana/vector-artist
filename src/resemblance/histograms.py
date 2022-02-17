import numpy as np
import cv2 as cv


def histogram(img: np.ndarray):
    hist = cv.calcHist([img], channels=[0, 1, 2], mask=None, histSize=[256, 256, 256], ranges=[0, 256, 0, 256, 0, 256])
    norm_hist = cv.normalize(hist, hist, alpha=0, beta=1, norm_type=cv.NORM_MINMAX).flatten()
    return norm_hist


def compare(img1: np.ndarray, img2: np.ndarray) -> float:
    hist1 = histogram(img1)
    hist2 = histogram(img2)
    return -cv.compareHist(hist1, hist2, method=cv.HISTCMP_CHISQR_ALT)


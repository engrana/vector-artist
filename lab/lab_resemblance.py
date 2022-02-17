import cv2 as cv
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from src.resemblance import hu_moments, histograms


def load_images_from_file_and_compare(path1, path2):

    img1 = np.array(Image.open(path1))
    print("Loaded image", path1)
    img2 = np.array(Image.open(path2))
    print("Loaded image", path2)

    # Using HuMoments shapes comparison. The score is a negative error (0 is a perfect match)
    print("Comparing by HuMoments...")
    start = time.time()
    score = hu_moments.compare(img1, img2)
    end = time.time()
    print("HuMoments results:", score, "(took", end - start, "seconds)")

    # Using color histograms comparison. The score is a negative error (0 is a perfect match)
    print("Comparing by Histograms...")
    start = time.time()
    score = histograms.compare(img1, img2)
    end = time.time()
    print("Histograms results:", score, "(took", end - start, "seconds)")


def load_image_find_contours(path):
    grayscale = np.array(Image.open(path).convert('L'))
    _, thresh = cv.threshold(grayscale, thresh=127, maxval=255, type=cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    img_contours = grayscale.copy()
    cv.drawContours(img_contours, contours, contourIdx=-1, color=(0, 255, 0),
                    thickness=2, lineType=cv.LINE_AA, hierarchy=hierarchy)
    fig, ax = plt.subplots()
    ax.imshow(img_contours)
    plt.show()


if __name__ == '__main__':
    load_images_from_file_and_compare(
        "./resources/images/input/mona-lisa-original.jpg",
        "./resources/images/input/mona-lisa-artwork.jpg"
    )
    # load_images_from_file_and_compare(
    #     "./resources/images/input/mona-lisa-original.jpg",
    #     "./resources/images/output/drawing.png"
    # )
    # load_image_find_contours("./resources/images/input/mona-lisa-original.jpg")
    # load_image_find_contours("./resources/images/input/mona-lisa-artwork.jpg")

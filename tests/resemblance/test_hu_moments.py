from unittest import TestCase
import numpy as np
from PIL import Image
import src.resemblance.hu_moments as hu_moments


class TestHuMoments(TestCase):

    def test_eval_hu_moments(self):
        """ Test calculating Hu-moments of a sample image """
        img = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        result = hu_moments.normalize(hu_moments.hu_moments(img))
        expected = [-0.49, -1.16, -3.35, -3.28, -6.59, -3.86, -7.98]
        for i in range(7):
            self.assertAlmostEqual(expected[i], result[i], places=2)

    def test_compare_histogram_with_self(self):
        """ Test comparing two Hu-moments of same image """
        img1 = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        img2 = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        result = hu_moments.compare(img1, img2)
        self.assertEqual(0, result)

    def test_compare_histogram_with_close(self):
        """ Test comparing two Hu-moments of images that should be close by colors resemblance """
        img1 = np.array(Image.open("../resources/flag_netherlands.png").convert("RGB"))
        img2 = np.array(Image.open("../resources/flag_germany.png").convert("RGB"))
        result = hu_moments.compare(img1, img2)
        self.assertAlmostEqual(-1200, result, places=1)

    def test_compare_histogram_with_far(self):
        """ Test comparing two Hu-moments of images that should be far by colors resemblance """
        img1 = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        img2 = np.array(Image.open("../resources/flag_netherlands.png").convert("RGB"))
        result = hu_moments.compare(img1, img2)
        self.assertAlmostEqual(-142.8, result, places=1)

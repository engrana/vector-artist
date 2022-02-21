from unittest import TestCase
import numpy as np
from PIL import Image
import src.resemblance.histograms as histograms


class TestHistograms(TestCase):

    def test_eval_histogram(self):
        """ Test calculating histogram of a sample image """
        img = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        result = histograms.histogram(img)
        self.assertEqual(0.0, np.min(result))
        self.assertEqual(1.0, np.max(result))
        self.assertEqual(32768, np.size(result))
        self.assertAlmostEqual(2.074, float(np.sum(result)), places=3)

    def test_compare_histogram_with_self(self):
        """ Test comparing two histograms of same image """
        img1 = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        img2 = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        result = histograms.compare(img1, img2)
        self.assertEqual(0, result)

    def test_compare_histogram_with_close(self):
        """ Test comparing two histograms of images that should be close by colors resemblance """
        img1 = np.array(Image.open("../resources/flag_germany.png").convert("RGB"))
        img2 = np.array(Image.open("../resources/flag_netherlands.png").convert("RGB"))
        result = histograms.compare(img1, img2)
        self.assertAlmostEqual(-8.3, result, places=1)

    def test_compare_histogram_with_far(self):
        """ Test comparing two histograms of images that should be far by colors resemblance """
        img1 = np.array(Image.open("../resources/flag_spain.png").convert("RGB"))
        img2 = np.array(Image.open("../resources/flag_netherlands.png").convert("RGB"))
        result = histograms.compare(img1, img2)
        self.assertAlmostEqual(-10.3, result, places=1)

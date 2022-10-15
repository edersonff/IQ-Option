import cv2 as cv
import numpy as np


class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        self.method = method

    def find(self, haystack_img, threshold=0.5, debug_mode=None):
        haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)
        needle_img = cv.cvtColor(self.needle_img, cv.COLOR_BGR2GRAY)

        result = cv.matchTemplate(haystack_img, needle_img, self.method)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            rectangles.append(rect)
            rectangles.append(rect)
        rectangle, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        if len(rectangle):
            return rectangle[0]
        return [0,0]

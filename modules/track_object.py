"""Different objects that can be tracked"""

import cv2

class NewObject:
    """
    A class that represents a trackable object

    Keyword arguments:
    size -- the width and height of the object (default 41)
    pos -- the position of the center of the object (default [0, 0])
    velo -- the velocity of the object (default [0, 0])
    img -- the path to the image
    """

    def __init__(self, img, size=41, pos=[0, 0], velo=[0, 0]):
        self.size = size
        self.img = cv2.resize(cv2.imread(img), [size, size])
        self.pos = pos
        self.velo = velo

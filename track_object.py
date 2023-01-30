"""Different objects that can be tracked"""

import numpy as np
import cv2

class FaceObject:
    """
    A class that represents a face

    Keyword arguments:
    size -- the width and height of the object (default 20)
    pos -- the position of the object (default [0, 0])
    velo -- the velocity of the object (default [0, 0])
    face -- the path to the face image
    """

    def __init__(self, face, size=20, pos=[0, 0], velo=[0, 0]):
        self.size = size
        self.face = cv2.resize(cv2.imread(face)[190:390,190:390],[size,size])
        self.pos = pos
        self.velo = velo

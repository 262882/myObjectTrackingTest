#!/usr/bin/env python3

import sys
sys.path.append('../')
import track_object
import cv2

# Try some parameters
SIZE = 30
POS = [1, 1]
VEL = [2, 2]

newFace = track_object.FaceObject('../lenna.png', SIZE, POS, VEL)
cv2.imwrite("test_face.jpg", newFace.face)

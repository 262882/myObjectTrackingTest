#!/usr/bin/env python3
"""Test case for basic function"""

import sys
sys.path.append('../modules')
import cv2
import track_object

# Try some parameters
SIZE = 31
POS = [1, 1]
VEL = [2, 2]

newFace = track_object.NewObject('../image/crop_lenna.png', SIZE, POS, VEL)
cv2.imwrite("test_face.jpg", newFace.img)

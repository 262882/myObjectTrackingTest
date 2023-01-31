#!/usr/bin/env python3
"""
Command line cropping

Command line arguments:
[1] -- the image to be cropped
[2] -- the upper left m axis
[3] -- the upper left n axis
[4] -- the bottom right m axis
[5] -- the bottom right n axis
"""

import sys
import cv2

upper_left = [int(sys.argv[2]), int(sys.argv[4])]
lower_right = [int(sys.argv[3]), int(sys.argv[5])]
cropped_img = cv2.imread(sys.argv[1])[upper_left[0]:lower_right[0], upper_left[1]:lower_right[1]]
cv2.imwrite("crop_"+sys.argv[1], cropped_img)

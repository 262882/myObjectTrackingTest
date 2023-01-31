#!/usr/bin/env python3
"""Test case for basic function"""

import sys
sys.path.append('../modules')
import cv2
import maze_gen


# Try some parameters
HEIGHT = 120
WIDTH = 180
NUM_OBS = 8

myMap = maze_gen.NewMap(HEIGHT, WIDTH, NUM_OBS)
cv2.imwrite("test_map.jpg", myMap.map)

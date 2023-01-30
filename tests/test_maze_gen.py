#!/usr/bin/env python3

import sys
sys.path.append('../')
import maze_gen
from matplotlib import pyplot as plt

# Try some parameters
HEIGHT = 120
WIDTH = 180
NUM_OBS = 8

myMap = maze_gen.NewMap(HEIGHT, WIDTH, NUM_OBS)
plt.imsave("test_map.jpg", myMap.map, cmap="gray")

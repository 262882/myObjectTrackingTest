#!/usr/bin/env python3

import sys
sys.path.append('../')
import maze_gen
from matplotlib import pyplot as plt

# Try some parameters
height = 120
width = 180
num_obstacles = 8

myMap = maze_gen.NewMap(m=height,n=width,n_obstacles=num_obstacles)
plt.imsave("test_map.jpg",myMap.map,cmap="gray")

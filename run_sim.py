#!/usr/bin/env python3
"""Start tracking video generator"""

import cv2
import sys
sys.path.append('./modules')
import world_model

print("Welcome to the Object Tracking Test Generator")

print("Initialising simulator")
objects = [
    ['./image/sunflower.tif', [-2, 2]],
    ['./image/face.png', [2, -2]],
    ['./image/parrot.jpg', [-2, -2]],
    ['./image/crop_lenna.png', [2, 2]]
    ]

test_sim = world_model.NewWorld(objects, obj_size=81, height=480, width=640, background='./image/hill.jpg')

# Set capture parameters
print("Start recording")
FPS = 30 # Capture rate
duration = 10 # seconds
video = cv2.VideoWriter('./tracking_test.avi', cv2.VideoWriter_fourcc(*'MP42'),
                        float(FPS), (test_sim.canvas.shape[1], test_sim.canvas.shape[0]))

# Main loop
for frame in range(FPS*duration):
    print("Process frame: " + str(frame))
    video.write(test_sim.canvas)
    test_sim.step()

video.release()
print("Complete")

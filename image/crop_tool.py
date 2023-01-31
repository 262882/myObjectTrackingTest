#!/usr/bin/env python3
import sys
import cv2

upper_left = [int(sys.argv[2]),int(sys.argv[4])]
lower_right = [int(sys.argv[3]),int(sys.argv[5])]
cropped_img = cv2.imread(sys.argv[1])[upper_left[0]:lower_right[0],upper_left[1]:lower_right[1]] 
cv2.imwrite("crop_"+sys.argv[1], cropped_img)

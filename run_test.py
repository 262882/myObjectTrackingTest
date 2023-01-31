#!/usr/bin/env python3
import world_model
import numpy as np
import cv2

if __name__ == '__main__':
	print("Welcome to the Object Tracking Test creator")

	print("Initialising simulator")
	test_sim = world_model.NewWorld('./image/crop_lenna.png')

	print("Start recording")
	FPS = 30
	duration = 10 #seconds
	video = cv2.VideoWriter('./test_result.avi', cv2.VideoWriter_fourcc(*'MP42'), float(FPS), (test_sim.canvas.shape[1], test_sim.canvas.shape[0]))

	# Main loop
	for frame in range(FPS*duration):
		print("Process frame: " + str(frame))
		cv2.imwrite("test1.jpg", test_sim.canvas)
		
		# Add graphics
		#canvas = cv2.putText(canvas, str(myObj.bounce), (myObj.pos[1],myObj.pos[0]), font, 1, color)
		video.write(test_sim.canvas)
		test_sim.step()
		
	video.release()
	print("Complete")

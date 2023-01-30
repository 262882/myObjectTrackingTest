#!/usr/bin/env python3

import maze_gen
import track_object
import numpy as np
import cv2

if __name__ == '__main__':
	print("Welcome to the Object Tracking Test")

	print("Initialising tracking object")
	myObj = track_object.FaceObject('./lenna.png')
	myObj.pos = [myObj.size,myObj.size]
	myObj.velo = [2,2]
	#font = cv2.FONT_HERSHEY_COMPLEX_SMALL
	#color = (255, 255, 255) 

	print("Generating map")
	myMaze = maze_gen.NewMap()

	# Generate until valid map (No initial clash)
	top_left = [myObj.pos[0]-myObj.size//2, myObj.pos[1]-myObj.size//2]
	initial_occupancy = myMaze.map[top_left[0]:top_left[0]+myObj.size, top_left[1]:top_left[1]+myObj.size]
	sum_empty = 3*255*(myObj.size)**2

	while np.sum(initial_occupancy) != sum_empty:
		myMaze = maze_gen.NewMap()

	print("Start visualisation")
	FPS = 30
	duration = 10 #seconds
	video = cv2.VideoWriter('./test_result.avi', cv2.VideoWriter_fourcc(*'MP42'), float(FPS), (myMaze.map.shape[1], myMaze.map.shape[0]))

	# Main loop
	for frame in range(FPS*duration):

		# Update ball position
		myObj.pos = [myObj.pos[0] + myObj.velo[0],myObj.pos[1] + myObj.velo[1]]
		
		# Update ball velocity if touch boundary
		if (myObj.pos[0] + myObj.size//2) >= myMaze.map.shape[0]:
			myObj.velo[0] = -myObj.velo[0]

		if (myObj.pos[1] + myObj.size//2) >= myMaze.map.shape[1]:
			myObj.velo[1] = -myObj.velo[1]

		if (myObj.pos[0] - myObj.size//2) <= 0:
			myObj.velo[0] = -myObj.velo[0]

		if (myObj.pos[1] - myObj.size//2) <= 0:
			myObj.velo[1] = -myObj.velo[1]
		
		# Update world
		canvas = np.copy(myMaze.map)
		canvas[myObj.pos[0]-myObj.size//2:myObj.pos[0]+myObj.size//2, myObj.pos[1]-myObj.size//2:myObj.pos[1]+myObj.size//2] = myObj.face
	
		video.write(canvas)
		
video.release()
print("Complete")


#!/usr/bin/env python3

import maze_gen
import track_object
import numpy as np
import cv2

if __name__ == '__main__':
	print("Welcome to the Object Tracking Test")

	print("Initialising tracking object")
	myObj = track_object.FaceObject('./lenna.png')
	myObj.pos = [myObj.size*2,myObj.size*2]
	myObj.velo = [2,2]
	#font = cv2.FONT_HERSHEY_COMPLEX_SMALL
	#color = (255, 255, 255) 

	print("Generating map")
	myMaze = maze_gen.NewMap()

	# Generate until valid map (No initial clash)
	top_left = [myObj.pos[0]-myObj.size//2, myObj.pos[1]-myObj.size//2]
	curr_occupancy = myMaze.map[top_left[0]:top_left[0]+myObj.size, top_left[1]:top_left[1]+myObj.size]
	sum_empty = 3*255*(myObj.size)**2
	sum_edge = 3*255*(myObj.size)   # Count edge of object, ignore corners

	while np.sum(curr_occupancy) != sum_empty:
		myMaze = maze_gen.NewMap()
		curr_occupancy = myMaze.map[top_left[0]:top_left[0]+myObj.size, top_left[1]:top_left[1]+myObj.size]

	print("Start visualisation")
	FPS = 30
	duration = 10 #seconds
	video = cv2.VideoWriter('./test_result.avi', cv2.VideoWriter_fourcc(*'MP42'), float(FPS), (myMaze.map.shape[1], myMaze.map.shape[0]))

	# Main loop
	for frame in range(FPS*duration):
		print(frame)

		# Update ball position
		myObj.pos = [myObj.pos[0] + myObj.velo[0],myObj.pos[1] + myObj.velo[1]]
		
		# Update ball velocity if edge touch obstacle
		# Bottom
		if np.sum(myMaze.map[myObj.pos[0]+myObj.size//2+myObj.velo[0], myObj.pos[1]-myObj.size//2-1:myObj.pos[1]+myObj.size//2]) < sum_edge:
			myObj.velo[0] = -myObj.velo[0]
		
		# Right
		if np.sum(myMaze.map[myObj.pos[0]-myObj.size//2-1:myObj.pos[0]+myObj.size//2, myObj.pos[1]+myObj.size//2+myObj.velo[1]]) < sum_edge:
			myObj.velo[1] = -myObj.velo[1]
		
		# Top
		if np.sum(myMaze.map[myObj.pos[0]-myObj.size//2-1+myObj.velo[0], myObj.pos[1]-myObj.size//2-1:myObj.pos[1]+myObj.size//2]) < sum_edge:
			myObj.velo[0] = -myObj.velo[0]
		
		# Left
		if np.sum(myMaze.map[myObj.pos[0]-myObj.size//2-1:myObj.pos[0]+myObj.size//2, myObj.pos[1]-myObj.size//2-1+myObj.velo[1]]) < sum_edge:
			myObj.velo[1] = -myObj.velo[1]
		
		# Update world
		canvas = np.copy(myMaze.map)  # Fetch blank map
		canvas[myObj.pos[0]-myObj.size//2-1:myObj.pos[0]+myObj.size//2, myObj.pos[1]-myObj.size//2-1:myObj.pos[1]+myObj.size//2] = myObj.face
		
		# Add graphics
		#canvas = cv2.putText(canvas, str(myObj.bounce), (myObj.pos[1],myObj.pos[0]), font, 1, color)
		video.write(canvas)
		
video.release()
print("Complete")


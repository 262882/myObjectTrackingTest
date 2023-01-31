"""Manages the world model"""

import maze_gen
import track_object
import numpy as np

class NewWorld:
    """
    A class that represents a world space

    Keyword arguments:
    size -- the width and height of the object (default 41)
    pos -- the position of the center of the object (default [0, 0])
    velo -- the velocity of the object (default [0, 0])
    img -- the path to the image
    """

    def __init__(self, img, size=41, pos=[0, 0], velo=[0, 0]):

        self.sum_empty = 3*255*(size)**2
        self.sum_edge = 3*255*(size)          # Count edge of object, ignore corners
        self.object_list = []
        self.add_object(img)

        # Generate until valid map (No initial clash)
        self.myMaze = maze_gen.NewMap()
        top_left = [self.object_list[0].pos[0]-self.object_list[0].size//2-1, self.object_list[0].pos[1]-self.object_list[0].size//2-1]
        curr_occupancy = self.myMaze.map[top_left[0]:top_left[0]+self.object_list[0].size, top_left[1]:top_left[1]+self.object_list[0].size]
        while np.sum(curr_occupancy) != self.sum_empty:
            self.myMaze = maze_gen.NewMap()
            curr_occupancy = self.myMaze.map[top_left[0]:top_left[0]+self.object_list[0].size, top_left[1]:top_left[1]+self.object_list[0].size]

        self.canvas = self.myMaze.map

    def add_object(self,path,vel=[2,2]):
        self.object_list.append(track_object.NewObject(path))
        self.object_list[-1].pos = [self.object_list[-1].size*2,self.object_list[-1].size*2]
        self.object_list[-1].velo = vel

    def update_pos(self):
        for obj in self.object_list:
            obj.pos = [obj.pos[0] + obj.velo[0],obj.pos[1] + obj.velo[1]]
    
    def update_collisions(self):
        for obj in self.object_list:
            # Bottom
            if np.sum(self.myMaze.map[obj.pos[0]+obj.size//2+obj.velo[0], obj.pos[1]-obj.size//2-1:obj.pos[1]+obj.size//2]) < self.sum_edge:
                obj.velo[0] = -obj.velo[0]
            # Right
            if np.sum(self.myMaze.map[obj.pos[0]-obj.size//2-1:obj.pos[0]+obj.size//2, obj.pos[1]+obj.size//2+obj.velo[1]]) < self.sum_edge:
                obj.velo[1] = -obj.velo[1]
            # Top
            if np.sum(self.myMaze.map[obj.pos[0]-obj.size//2-1+obj.velo[0], obj.pos[1]-obj.size//2-1:obj.pos[1]+obj.size//2]) < self.sum_edge:
                obj.velo[0] = -obj.velo[0]
            # Left
            if np.sum(self.myMaze.map[obj.pos[0]-obj.size//2-1:obj.pos[0]+obj.size//2, obj.pos[1]-obj.size//2-1+obj.velo[1]]) < self.sum_edge:
                obj.velo[1] = -obj.velo[1]

    def update_world(self):
        self.canvas = np.copy(self.myMaze.map)  # Fetch blank map
        for obj in self.object_list:
            self.canvas[obj.pos[0]-obj.size//2-1:obj.pos[0]+obj.size//2, obj.pos[1]-obj.size//2-1:obj.pos[1]+obj.size//2] = obj.img

    def step(self):
        self.update_pos()
        self.update_collisions()
        self.update_world()


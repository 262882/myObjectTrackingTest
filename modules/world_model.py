"""Manages the world model"""

import maze_gen
import track_object
import numpy as np

class NewWorld:
    """
    A class that represents a world space

    Keyword arguments:
    def_obj -- A list of objects of the form [path,[vertical velocity, horizontal velocity]]
    obj_size -- the size of the objects
    height -- the height of the map (default 240)
    width -- the width of the map (default 360)
    num_obstacles -- the number of obstuctions generated (default 5)
    thickness_wall -- the thickness of the obstructuions (default 4)
    """

    def __init__(self, def_obj, obj_size=41, height=240, width=360, num_obstacles=5, thickness_wall=4):

        # Evaluate checksums 
        self.sum_empty = 3*255*(obj_size)**2
        self.sum_edge = 3*255*(obj_size)          # Count edge of object, ignore corners

        # Load objects
        self.object_list = []
        for entry in def_obj:
            self.__add_object(entry[0],obj_size,[height//2,width//2], entry[1])

        # Generate until valid map (No initial clash)
        self.myMaze = maze_gen.NewMap(m=height, n=width, n_obstacles=num_obstacles, t_wall=thickness_wall)
        top_left = [self.object_list[0].pos[0]-self.object_list[0].size//2-1, self.object_list[0].pos[1]-self.object_list[0].size//2-1]
        curr_occupancy = self.myMaze.map[top_left[0]:top_left[0]+self.object_list[0].size, top_left[1]:top_left[1]+self.object_list[0].size]
        while np.sum(curr_occupancy) != self.sum_empty:
            self.myMaze = maze_gen.NewMap(m=height, n=width, n_obstacles=num_obstacles, t_wall=thickness_wall)
            curr_occupancy = self.myMaze.map[top_left[0]:top_left[0]+self.object_list[0].size, top_left[1]:top_left[1]+self.object_list[0].size]
        self.canvas = self.myMaze.map

    def __add_object(self,path,size=41, pos=[0,0],vel=[0,0]):
        self.object_list.append(track_object.NewObject(path, size, pos, vel))
        self.object_list[-1].pos = pos
        self.object_list[-1].velo = vel

    def __update_pos(self):
        for obj in self.object_list:
            obj.pos = [obj.pos[0] + obj.velo[0],obj.pos[1] + obj.velo[1]]
    
    def __update_collisions(self):
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

    def __update_world(self):
        self.canvas = np.copy(self.myMaze.map)  # Fetch blank map
        for obj in self.object_list:
            self.canvas[obj.pos[0]-obj.size//2-1:obj.pos[0]+obj.size//2, obj.pos[1]-obj.size//2-1:obj.pos[1]+obj.size//2] = obj.img

    def step(self):
        self.__update_pos()
        self.__update_collisions()
        self.__update_world()


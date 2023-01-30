"""Random maze generator"""

import numpy as np

class NewMap:
    """
    A random maze with obstacles

    Keyword arguments:
    m -- the height of the maze (default 240)
    n -- the width of the maze (default 360)
    n_obstacles -- the number of obstacles (default 5)
    t_wall -- the thickness of obstacle wall (default 4)
    """

    def __init__(self, m=240, n=360, n_obstacles=5, t_wall=4):
        self.map = np.ones([m, n, 3], dtype='uint8')*255  # OpenCV needs 3 channel image
        self.t_wall = t_wall

        # Insert obstacles
        for obs in self.__obstacle_list(n_obstacles):
            self.__insert_obstacle(obs[0], obs[1])

    def __insert_obstacle(self, coord1, coord2):
        """ Insert an obstacle from start to end """
        t_w = self.t_wall
        self.map[coord1[0]-t_w//2:coord2[0]+1+t_w//2, coord1[1]-t_w//2:coord2[1]+1+t_w//2, :] = 0

    def __obstacle_list(self, n_obstacles):
        """ Generate a list of randomly generated vertical and horizonal obstacles """
        obs_list = []
        randbit_gen = np.random.bit_generator

        for _ in range(n_obstacles):
            orient = randbit_gen.randbits(1)     # Assign a vertical or horizontal orientation

            rand_len = np.random.randint(5, max(self.map.shape))     # Assign a length
            start_coordm = np.random.randint(0, self.map.shape[0])  # Assign a starting vert coord
            start_coordn = np.random.randint(0, self.map.shape[1])  # Assign a starting horiz coord

            # Dont allow assigning obstacles outside of map
            end_coordm = min(start_coordm+rand_len*(1-orient), self.map.shape[0])
            end_coordn = min(start_coordn+rand_len*orient, self.map.shape[1])

            obs_list.append(np.array([[start_coordm, start_coordn], [end_coordm, end_coordn]]))

        return obs_list

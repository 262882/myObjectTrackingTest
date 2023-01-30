import numpy as np

class map:
    """
    A random maze with obstacles 

    Keyword arguments:
    m -- the height of the maze (default 240)
    n -- the width of the maze (default 360)
    n_obstacles -- the number of obstacles (default 5)
    t_wall -- the thickness of obstacle wall (default 4)
    """

    def __init__(self,m=240,n=360, n_obstacles=5, t_wall = 4):
        self.map = np.ones([m,n,3],dtype='uint8')*255  # OpenCV needs 3 channel image
        self.t_wall = t_wall

        # Insert obstacles
        for obs in self.__obstacle_list(n_obstacles):
            self.__insert_obstacle(obs[0],obs[1])

    def __insert_obstacle(self,coord1,coord2):
        """ Insert an obstacle from start to end """
        self.map[coord1[0]-self.t_wall//2:coord2[0]+1+self.t_wall//2,coord1[1]-self.t_wall//2:coord2[1]+1+self.t_wall//2,:]=0
        
    def __obstacle_list(self,n_obstacles):
        """ Generate a list of randomly generated vertical and horizonal obstacles """
        obs_list = []
        randBitGen = np.random.bit_generator

        for i in range(n_obstacles):
            orient = randBitGen.randbits(1)     # Assign a vertical or horizontal orientation

            randLen = np.random.randint(5,max(self.map.shape))      # Assign a length
            randCoordm = np.random.randint(0,self.map.shape[0])      # Assign a starting vertical coordinate 
            randCoordn = np.random.randint(0,self.map.shape[1])      # Assign a starting horizontal coordinate 

            obs_list.append(np.array([[randCoordm,randCoordn],[min(randCoordm+randLen*(1-orient),self.map.shape[0]),min(randCoordn+randLen*orient,self.map.shape[1])]]))
        
        return obs_list
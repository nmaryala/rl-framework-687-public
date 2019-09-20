import numpy as np
from .skeleton import Environment
np.random.seed(0)

class Gridworld(Environment):
    """
    The Gridworld as described in the lecture notes of the 687 course material. 
    
    Actions: up (0), down (1), left (2), right (3)
    
    Environment Dynamics: With probability 0.8 the robot moves in the specified
        direction. With probability 0.05 it gets confused and veers to the
        right -- it moves +90 degrees from where it attempted to move, e.g., 
        with probability 0.05, moving up will result in the robot moving right.
        With probability 0.05 it gets confused and veers to the left -- moves
        -90 degrees from where it attempted to move, e.g., with probability 
        0.05, moving right will result in the robot moving down. With 
        probability 0.1 the robot temporarily breaks and does not move at all. 
        If the movement defined by these dynamics would cause the agent to 
        exit the grid (e.g., move up when next to the top wall), then the
        agent does not move. The robot starts in the top left corner, and the 
        process ends in the bottom right corner.
        
    Rewards: -10 for entering the state with water
            +10 for entering the goal state
            0 everywhere else
        
    
    
    """

    def __init__(self, startState=0, endState=24, shape=(5,5), obstacles=[12, 17], waterStates=[6, 18, 22]):
        # initialize(startState, endState, obstacles, waterStates)
        self.name = "Gridworld"
        self.state = startState
        self.isEnd = (self.state == endState)
        self.waterStates = waterStates
        self.endState = endState
        self.gamma = 0.9
        self.p = self.populateP()
        
    def name(self):
        pass
        
    def reward(self):
        pass

    def action(self):
        pass

    def isEnd(self):
        pass

    def state(self):
        pass

    def gamma(self):
        pass

    def waterStates(self):
        pass

    def endState(self):
        pass

    def p(self):
        pass
        

    def randomizeAction(self, action):
        newAction = -1
        if action == 0:
            newAction = np.random.choice(np.array([0,2,3,5]), p = [0.8, 0.05, 0.05, 0.1])
        if action == 1:
            newAction = np.random.choice(np.array([1,2,3,5]), p = [0.8, 0.05, 0.05, 0.1])
        if action == 2:
            newAction = np.random.choice(np.array([2,0,1,5]), p = [0.8, 0.05, 0.05, 0.1])
        if action == 3:
            newAction = np.random.choice(np.array([3,0,1,5]), p = [0.8, 0.05, 0.05, 0.1])
        return newAction

    def populateP(self):
        p = {}
        #Rules for staying
        for i in range(0,25):
            p[(i,5)] = i


        #Rules for moving up
        for i in range(0,25):
            p[i,0] = i-5

        for i in range(5):
            p[i,0] = i

        p[(22,0)] = 22
        p[(24,0)] = 24

        

        #Rules for moving down
        for i in range(0,25):
            p[i,1] = i+5

        for i in range(20,25):
            p[i,1] = i

        p[(7,1)] = 7
        p[(24,1)] = 24

        
        #Rules for moving left
        for i in range(0,25):
            p[i,2] = i-1

        p[(0,2)] = 0
        p[(5,2)] = 5
        p[(10,2)] = 10
        p[(15,2)] = 15
        p[(20,2)] = 20

        p[(13,2)] = 13
        p[(18,2)] = 18

        p[(24,2)] = 24

        
        #Rules for moving right
        for i in range(0,25):
            p[i,3] = i+1

        p[(4,3)] = 4
        p[(9,3)] = 9
        p[(14,3)] = 14
        p[(19,3)] = 19

        p[(11,3)] = 11
        p[(16,3)] = 16

        p[(24,3)] = 24

        return p

    def step(self, action):
        newAction = self.randomizeAction(action)
        newState = self.p[(self.state, newAction)]
        self.state = newState
        if self.state == 24:
            self.reward = 10
            self.isEnd = True
        elif self.state in self.waterStates:
            self.reward = -10
            self.isEnd = False
        else:
            self.reward = 0
            self.isEnd = False      

    def reset(self):
        self.__init__()
        
    def R(self, _state):
        """
        reward function
        
        output:
            reward -- the reward resulting in the agent being in a particular state
        """
        if _state in self.waterStates:
            return -10
        if _state == self.endState:
            return 10
        else:
            return 0

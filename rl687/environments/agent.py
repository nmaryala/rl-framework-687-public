import numpy as np
np.random.seed(0)
from abc import ABC, abstractmethod

class Agent(ABC):

    def __init__(self):
        self.popluatePi()
    
    @property
    def name(self):
        pass

    def pi(self):
        pass

    def popluatePi(self):
        pi = {}
        pi[0] = 3
        pi[1] = 3
        pi[2] = 3
        pi[3] = 3
        pi[4] = 1
        pi[5] = 0
        pi[6] = 3
        pi[7] = 3
        pi[8] = 3
        pi[9] = 1
        pi[10] = 0
        pi[11] = 2 #Avoiding 0.05 chance of water drop if we put 3
        pi[12] = 3
        pi[13] = 3
        pi[14] = 1
        pi[15] = 0
        pi[16] = 2
        pi[17] = 2
        pi[18] = 3
        pi[19] = 1
        pi[20] = 0
        pi[21] = 2
        pi[22] = 3
        pi[23] = 3
        pi[24] = 5
        self.pi = pi

    # def popluatePiPositivePolicy(self):
    #     pi = {}
    #     pi[0] = 0
    #     pi[1] = 0
    #     pi[2] = 0
    #     pi[3] = 0
    #     pi[4] = 1
    #     pi[9] = 3
    #     pi[14] = 3
    #     pi[19] = 3
    #     pi[24] = 5
    #     self.pi = pi

    def act(self):
        return np.random.choice(np.array([0,1,2,3]))

    def actOptimally(self, state):
        return self.pi[state]        
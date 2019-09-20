import numpy as np
import statistics as st
from rl687.environments.gridworld import Gridworld
from rl687.environments.agent import Agent
import matplotlib.pyplot as plt

def problemA(num_iters):
    """
    Have the agent uniformly randomly select actions. Run 10,000 episodes.
    Report the mean, standard deviation, maximum, and minimum of the observed 
    discounted returns.
    """
    agent = Agent()
    discounted_returns = []
    gridworld = Gridworld()

    for i in range(num_iters):
        reward = 0
        time = 0
        while True:
            action = agent.act()
            gridworld.step(action)
            reward += gridworld.reward * (gridworld.gamma**time)
            if gridworld.isEnd:
                break
            time += 1
        discounted_returns.append(reward)
        gridworld.reset()

    print('Mean = ',st.mean(discounted_returns))
    print('Standard deviation = ',st.stdev(discounted_returns))
    print('Max = ',max(discounted_returns))
    print('Min = ',min(discounted_returns))

    return discounted_returns

def problemC(num_iters):
    """
    Find an optimal policy (you may do this any way you choose,
    including by reasoning through the problem yourself). Report the optimal
    policy here. Comment on whether it is unique
    """
    agent = Agent()
    discounted_returns = []
    gridworld = Gridworld()
    print("acting optimally")

    for i in range(num_iters):
        reward = 0
        time = 0
        while True:
            action = agent.actOptimally(gridworld.state)
            gridworld.step(action)
            reward += gridworld.reward * (gridworld.gamma**time)
            if gridworld.isEnd:
                break
            time += 1
        discounted_returns.append(reward)
        gridworld.reset()

    print('Mean = ',st.mean(discounted_returns))
    print('Standard deviation = ',st.stdev(discounted_returns))
    print('Max = ',max(discounted_returns))
    print('Min = ',min(discounted_returns))    

    return discounted_returns

    
def problemD(num_iters):
    """
    Plot the distribution of returns for both the random policy and the optimal
    policy using 10,000 trials each. You must clearly label each line and axis.
    Additionally, report the random seed used for the experiments
    """
    random_results = problemA(num_iters)
    optimal_results = problemC(num_iters)

    (x,y) = CDF(random_results)
    (x1,y1) = CDF(optimal_results)
    plt.grid(True, axis='x') # let's add a grid on y-axis
    plt.title('Distribution of returns for various policies with Seed 0 and 10000 iters', fontsize=18) # chart title
    plt.plot(y, x, 'r', label = 'random policy')
    plt.plot(y1,x1, 'g', label = 'optimal policy')
    plt.ylabel('Expected returns')
    plt.xlabel('Probability')
    plt.legend(loc='best')
    plt.show()

    # boxPlot(random_results, optimal_results)

def CDF(x):
    x.sort()   
    y = []
    for i in range(len(x)):
        y.append((i+1)/len(x))

    return (x, y)

def boxPlot(random_results, optimal_results):
    results = [random_results, optimal_results]
    box = plt.boxplot(results, showmeans=True, whis=50, meanline = True)
    plt.setp(box['boxes'][0], color='blue')
    plt.setp(box['boxes'][1], color='green')
    plt.grid(True, axis='y') # let's add a grid on y-axis
    plt.title('Distribution of returns for various policies with Seed 0', fontsize=18) # chart title
    plt.ylabel('Expected Returns') # y axis title
    plt.xticks([1,2], ['Random','Optimal']) # x axis labels
    plt.show()
    

def problemE(num_iters):
    agent = Agent()
    gridworld = Gridworld()
    count = 0

    for i in range(num_iters):
        gridworld.state = 19 #defining the state to be above end
        for i in range(8,19):
            time = i #not used anywhere, just for clarity purpose
            action = agent.act() #this will be action a_18 in the last iteration
            gridworld.step(action)

        if gridworld.state == 22:
            count += 1

    print('P(S_19 = 22| S_8=19) = ', count/num_iters)


def Main():
    num_iters = 10000
    #problemA(num_iters)
    #problemC(num_iters)
    #problemD(num_iters)
    problemE(num_iters)

Main()
        
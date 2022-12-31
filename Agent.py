import numpy as np

class Agent(object):
    def __init__(self, states, num, alpha=0.15, random_factor=0.2):  # 80% explore, 20% exploit
        self.stateHistory = [((0, 0), 0)]  # state, reward
        self.alpha = alpha
        self.randomFactor = random_factor
        self.G = {}
        self.init_reward(states)
        self.num = num

    def init_reward(self, states):
        for state in states:
                self.G[state] = np.random.uniform(high=1.0, low=0.1)
    def choose_action(self, state, allowedMoves):
        maxG = -10e15
        next_move = None
        randomN = np.random.random()
        if randomN < self.randomFactor:
            # if random number below random factor, choose random action
            next_move = allowedMoves[np.random.choice(len(allowedMoves),1)[0]]
        else:
            # if exploiting, gather all possible actions and choose one with the highest G (reward)
            for action in allowedMoves:
                try:
                    if self.G[action] >= maxG:
                        next_move = action
                        maxG = self.G[action]
                except:
                    print("UHOH")

        return next_move

    def update_state_history(self, state, reward):
        self.state_history.append((state, reward))

    def learn(self):
        target = 0

        for prev, reward in reversed(self.state_history):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward

        self.state_history = []

        self.random_factor -= 10e-5  # decrease random factor each episode of play

    def __repr__(self):
        return f"Agent {self.num}"

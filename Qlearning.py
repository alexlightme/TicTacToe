def learn(self, env):
    if env.env_name == "tictactoe":
        self.q_table = self.q_table(env)
        for i in range(self.epochs):
            state = env.reset()


epochs, reward, = 0, 0, 0
done = False
while done != True:
    if random.uniform(0, 1) < self.epsilon:
        action = env.action_space.sample()  # Explore action space
        # forbiden ilegal action
        while state[int(action / 3)][action % 3] != 0:
            action = env.action_space.sample()
    else:
        action_value_list = self.q_table[self.state_to_number(state)]
        for action, action_value in enumerate(action_value_list):
            if state[int(action / 3)][action % 3] != 0:
                action_value_list[action] = np.nan
        action = np.nanargmax(action_value_list)  # Exploit learned values
    next_state, reward, done, info = env.step(action)
    old_value = self.q_table[self.state_to_number(state), action]
    next_max = np.nanmax(self.q_table[self.state_to_number(next_state)])
    new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
    self.q_table[self.state_to_number(state), action] = new_value
    state = next_state
epochs += 1


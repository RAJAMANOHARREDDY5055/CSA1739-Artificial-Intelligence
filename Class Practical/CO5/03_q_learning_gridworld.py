"""Q-learning agent in a small deterministic 4x4 gridworld."""
import numpy as np
rng = np.random.default_rng(3)
N, ACTIONS = 4, 4  # up, right, down, left
start, goal = 0, 15
Q = np.zeros((N*N, ACTIONS))
def step(state, action):
    r, c = divmod(state, N)
    if action == 0: r = max(0, r-1)
    elif action == 1: c = min(N-1, c+1)
    elif action == 2: r = min(N-1, r+1)
    else: c = max(0, c-1)
    nxt = r*N+c
    return nxt, (10 if nxt == goal else -1), nxt == goal
alpha, gamma, epsilon = .2, .95, .15
for episode in range(2500):
    s = start
    for _ in range(100):
        a = rng.integers(ACTIONS) if rng.random() < epsilon else int(np.argmax(Q[s]))
        ns, reward, done = step(s, a)
        Q[s, a] += alpha * (reward + gamma*np.max(Q[ns])*(not done) - Q[s, a])
        s = ns
        if done: break
# Display greedy route
s, route = start, [start]
for _ in range(20):
    if s == goal: break
    s, _, _ = step(s, int(np.argmax(Q[s])))
    route.append(s)
print("Learned route (cell indexes):", route)

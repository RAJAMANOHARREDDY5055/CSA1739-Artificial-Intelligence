"""Genetic algorithm evolves weights of a tiny neural network for XOR.
Each chromosome contains weights for a 2-2-1 sigmoid network.
"""
import numpy as np
rng = np.random.default_rng(9)
X = np.array([[0,0],[0,1],[1,0],[1,1]], float)
Y = np.array([[0],[1],[1],[0]], float)
# 2x2 input weights, 2 hidden biases, 2 output weights, output bias = 9 genes
def sigmoid(z): return 1/(1+np.exp(-np.clip(z, -30, 30)))
def predict(g):
    w1 = g[:4].reshape(2,2); b1 = g[4:6]
    w2 = g[6:8].reshape(2,1); b2 = g[8]
    return sigmoid(sigmoid(X @ w1 + b1) @ w2 + b2)
def fitness(g): return -float(np.mean((predict(g)-Y)**2))
population = rng.normal(0, 1, (60, 9))
for generation in range(250):
    scores = np.array([fitness(g) for g in population])
    elite = population[np.argsort(scores)[-6:]]
    children = [e.copy() for e in elite]
    while len(children) < len(population):
        p1, p2 = elite[rng.integers(len(elite), size=2)]
        mask = rng.random(9) < .5
        child = np.where(mask, p1, p2) + rng.normal(0, .15, 9)
        children.append(child)
    population = np.array(children)
best = max(population, key=fitness)
print("Best fitness:", fitness(best))
print("XOR predictions:", np.round(predict(best).ravel(), 3))

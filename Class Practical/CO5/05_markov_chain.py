"""Markov chain for predicting the next weather state."""
import random
random.seed(1)
transitions = {
    "Sunny": [("Sunny", .7), ("Rainy", .3)],
    "Rainy": [("Sunny", .4), ("Rainy", .6)]
}
def next_state(current):
    r = random.random()
    cumulative = 0
    for state, probability in transitions[current]:
        cumulative += probability
        if r <= cumulative: return state
    return transitions[current][-1][0]

state = "Sunny"
sequence = [state]
for _ in range(10):
    state = next_state(state)
    sequence.append(state)
print("Predicted sample sequence:", " -> ".join(sequence))

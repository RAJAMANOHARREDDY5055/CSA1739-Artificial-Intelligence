"""Genetic algorithm maximizes f(x) = x^2 for integer x in [0, 31]."""
import random
random.seed(4)
POP, BITS, GENERATIONS = 12, 5, 40
def decode(chromosome): return int(chromosome, 2)
def fitness(chromosome): return decode(chromosome) ** 2
def select(pop):
    a, b = random.sample(pop, 2)
    return max(a, b, key=fitness)
population = [format(random.randrange(2**BITS), f"0{BITS}b") for _ in range(POP)]
for _ in range(GENERATIONS):
    new = [max(population, key=fitness)]  # elitism
    while len(new) < POP:
        p1, p2 = select(population), select(population)
        cut = random.randrange(1, BITS)
        child = p1[:cut] + p2[cut:]
        if random.random() < .1:
            i = random.randrange(BITS)
            child = child[:i] + ("1" if child[i] == "0" else "0") + child[i+1:]
        new.append(child)
    population = new
best = max(population, key=fitness)
print("Best x:", decode(best), "Fitness:", fitness(best))

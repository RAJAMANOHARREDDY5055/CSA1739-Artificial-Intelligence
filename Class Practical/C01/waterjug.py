
from collections import deque

def water_jug(cap1, cap2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == target or y == target:
            print("Target reached!")
            return

        next_states = [
            (cap1, y),                 # Fill jug 1
            (x, cap2),                 # Fill jug 2
            (0, y),                    # Empty jug 1
            (x, 0),                    # Empty jug 2
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("Solution not possible")

water_jug(4, 3, 2)

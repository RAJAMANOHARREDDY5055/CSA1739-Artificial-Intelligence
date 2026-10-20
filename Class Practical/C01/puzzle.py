
import heapq

def manhattan(state, goal):
    distance = 0

    for i, value in enumerate(state):
        if value != 0:
            j = goal.index(value)
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)

    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def solve(start, goal):
    pq = []
    heapq.heappush(pq, (manhattan(start, goal), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            for step in path:
                print(step[:3])
                print(step[3:])
                print()
            print("Goal reached!")
            print("Moves:", len(path) - 1)
            return

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(neighbor, goal)

                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No solution found")

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solve(start, goal)

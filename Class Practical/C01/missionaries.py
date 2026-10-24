from collections import deque

# State: (missionaries_left, cannibals_left, boat_position)
# Boat position: 0 = left bank, 1 = right bank

start = (3, 3, 0)
goal = (0, 0, 1)

moves = [(1, 0), (2, 0), (0, 1),
         (0, 2), (1, 1)]

def valid(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False

    mr, cr = 3 - m, 3 - c

    if m > 0 and c > m:
        return False

    if mr > 0 and cr > mr:
        return False

    return True

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Solution path:")
        for s in path:
            print(s)
        print("Goal reached!")
        break

    m, c, boat = state

    for dm, dc in moves:
        if boat == 0:
            new_state = (m - dm, c - dc, 1)
        else:
            new_state = (m + dm, c + dc, 0)

        if valid(new_state[0], new_state[1]):
            if (boat == 0 and dm <= m and dc <= c) or (
                boat == 1 and dm <= 3-m and dc <= 3-c
            ):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))
else:
    print("No solution found.")
from collections import deque

goal = 4

def water_jug_problem(capacity_a, capacity_b, goal):

    visited = set()
    queue = deque([(0, 0)])

    parent = { (0, 0): None }

    while queue:
        a, b = queue.popleft()

        if a == goal or b == goal:
            print("Goal reached! One of the jugs contains exactly", goal, "liters.")
            print("Steps taken to reach the goal:")

            path = []
            state = (a, b)
            while state is not None:
                path.append(state)
                state = parent[state]
            path.reverse()

            for i, (a_state, b_state) in enumerate(path):
                print(f"Step {i + 1}: Jug A = {a_state} liters, Jug B = {b_state} liters")
            return True

        visited.add((a, b))

        possible_moves = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
            (a - min(a, capacity_b - b), b + min(a, capacity_b - b)),
            (a + min(b, capacity_a - a), b - min(b, capacity_a - a))
        ]

        for new_a, new_b in possible_moves:
            if (new_a, new_b) not in visited:

                parent[(new_a, new_b)] = (a, b)
                queue.append((new_a, new_b))

    return False

capacity_a = 3
capacity_b = 5

if water_jug_problem(capacity_a, capacity_b, goal):
    print("\nSolution found!")
else:
    print("It is not possible to get exactly 4 liters with these jugs.")

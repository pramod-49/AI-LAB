import heapq
import numpy as np

goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None, g=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.g = g
        self.h = self.manhattan_distance()
        self.f = self.g + self.h

    def manhattan_distance(self):
        dist = 0
        for i in range(3):
            for j in range(3):
                tile = self.puzzle[i][j]
                if tile != 0:
                    goal_i, goal_j = divmod(tile - 1, 3)
                    dist += abs(goal_i - i) + abs(goal_j - j)
        return dist

    def get_neighbors(self):
        neighbors = []
        empty_pos = tuple(np.argwhere(self.puzzle == 0)[0])
        x, y = empty_pos

        for dx, dy in MOVES:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_puzzle = self.puzzle.copy()
                new_puzzle[x, y], new_puzzle[new_x, new_y] = new_puzzle[new_x, new_y], new_puzzle[x, y]
                neighbors.append(PuzzleState(new_puzzle, self, (x, y, new_x, new_y), self.g + 1))

        return neighbors

    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)

    def __lt__(self, other):
        return self.f < other.f

    def print_puzzle(self):
        for row in self.puzzle:
            print(' '.join(map(str, row)))
        print()

def a_star_search(initial_state):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if np.array_equal(current_state.puzzle, goal_state):
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]

        closed_set.add(tuple(current_state.puzzle.flatten()))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.puzzle.flatten()) not in closed_set:
                heapq.heappush(open_list, neighbor)

    return None

def print_solution(path):
    for state in path:
        state.print_puzzle()

initial_state = PuzzleState(np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]]))

solution_path = a_star_search(initial_state)

if solution_path:
    print("Solution found:")
    print_solution(solution_path)
else:
    print("No solution found.")

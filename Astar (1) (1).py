import heapq

# Define the goal state
goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)  # 0 represents the blank tile

# Define the possible moves for each tile
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != goal_state[i] and state[i] != 0:
            goal_index = goal_state.index(state[i])
            distance += abs(i % 3 - goal_index % 3) + abs(i // 3 - goal_index // 3)
    return distance

# Global variable to keep track of the order
encounter_order = 0

# Define the A* algorithm
def astar(start):
    global encounter_order
    open_list = []
    heapq.heappush(open_list, (0, encounter_order, start))
    g_values = {start: 0}
    came_from = {}

    while open_list:
        _, _, current = heapq.heappop(open_list)
        if current == goal_state:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        zero_index = current.index(0)
        for move in moves[zero_index]:
            new_state = list(current)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            new_state = tuple(new_state)
            tentative_g = g_values[current] + 1
            if new_state not in g_values or tentative_g < g_values[new_state]:
                g_values[new_state] = tentative_g
                f_value = tentative_g + heuristic(new_state)
                encounter_order += 1  # Increment the order for each encountered state
                heapq.heappush(open_list, (f_value, encounter_order, new_state))
                came_from[new_state] = current

# Test the algorithm with a sample puzzle
start_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)  # Initial state of the puzzle
solution_path = astar(start_state)
if solution_path:
    print("Solution found!")
    print("Number of steps:", len(solution_path))
    for step, state in enumerate(solution_path):
        print(f"Step {step + 1}:")
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution found!")
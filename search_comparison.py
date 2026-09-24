
import time
from collections import deque

# Board size
BOARD_SIZE = 8

# All possible moves of a knight
KNIGHT_MOVES = [
    (1, 2),
    (2, 1),
    (-1, 2),
    (-2, 1),
    (1, -2),
    (2, -1),
    (-1, -2),
    (-2, -1)
]

# Starting and target positions
START = (0, 0)   # a1
GOAL = (7, 7)    # h8


# Generate valid knight moves
def neighbors(position):
    x, y = position

    for dx, dy in KNIGHT_MOVES:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
            yield (nx, ny)


# Breadth-First Search
def bfs(start, goal):
    queue = deque([start])

    came_from = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for next_position in neighbors(current):
            if next_position not in came_from:
                came_from[next_position] = current
                queue.append(next_position)

    # Reconstruct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = came_from.get(node)

    path.reverse()

    return path, nodes_expanded


# Depth-First Search
def dfs(start, goal):
    stack = [start]

    came_from = {start: None}
    visited = {start}

    nodes_expanded = 0

    while stack:
        current = stack.pop()
        nodes_expanded += 1

        if current == goal:
            break

        for next_position in neighbors(current):
            if next_position not in visited:
                visited.add(next_position)
                came_from[next_position] = current
                stack.append(next_position)

    # Reconstruct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = came_from.get(node)

    path.reverse()

    return path, nodes_expanded


# Convert board coordinates into chess notation
def square_name(position):
    x, y = position
    return f"{chr(ord('a') + x)}{y + 1}"


# Run an algorithm multiple times and measure execution time
def time_algorithm(function, start, goal, runs=5):

    times = []
    path = None
    nodes = None

    for _ in range(runs):

        start_time = time.perf_counter()

        path, nodes = function(start, goal)

        end_time = time.perf_counter()

        time_taken = (end_time - start_time) * 1000
        times.append(time_taken)

    return {
        "path": path,
        "nodes_expanded": nodes,
        "times_ms": times,
        "best_ms": min(times),
        "worst_ms": max(times),
        "avg_ms": sum(times) / len(times)
    }


# Main program
if __name__ == "__main__":

    print("Knight's Shortest-Path Problem")
    print("=" * 60)

    print(
        f"Board: {BOARD_SIZE}x{BOARD_SIZE} | "
        f"Start: {square_name(START)} | "
        f"Goal: {square_name(GOAL)}"
    )

    print("=" * 60)

    # Run BFS
    bfs_result = time_algorithm(bfs, START, GOAL, runs=5)

    # Run DFS
    dfs_result = time_algorithm(dfs, START, GOAL, runs=5)

    # Display results
    for name, result in [
        ("BFS", bfs_result),
        ("DFS", dfs_result)
    ]:

        print(f"\n{name}")
        print("-" * 40)

        print(
            f"Path length (moves): "
            f"{len(result['path']) - 1}"
        )

        print(
            "Path: "
            + " -> ".join(
                square_name(position)
                for position in result["path"]
            )
        )

        print(
            f"Nodes expanded: "
            f"{result['nodes_expanded']}"
        )

        print(
            "Times (ms) over 5 runs: "
            + str(
                [round(time_value, 4)
                 for time_value in result["times_ms"]]
            )
        )

        print(
            f"Best: {result['best_ms']:.4f} ms"
        )

        print(
            f"Worst: {result['worst_ms']:.4f} ms"
        )

        print(
            f"Average: {result['avg_ms']:.4f} ms"
        )

    print("\n" + "=" * 60)
    print("BFS and DFS comparison completed successfully!")
from collections import deque
import heapq

def is_valid_move(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 0


def bfs(matrix, start, end):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    rows, cols = len(matrix), len(matrix[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    start_row, start_col = start
    end_row, end_col = end

    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True

    while queue:
        current_row, current_col = queue.popleft()

        if current_row == end_row and current_col == end_col:
            return construct_path(parent, start, end)

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if is_valid_move(matrix, new_row, new_col) and not visited[new_row][new_col]:
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[new_row][new_col] = (current_row, current_col)

    return []


def dfs(matrix, start, end):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    path = []

    def dfs_helper(row, col):
        nonlocal path
        if not is_valid_move(matrix, row, col) or visited[row][col]:
            return False

        visited[row][col] = True
        path.append((row, col))

        if (row, col) == end:
            return True

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and dfs_helper(new_row, new_col):
                return True

        path.pop()
        return False

    start_row, start_col = start
    if dfs_helper(start_row, start_col):
        return path
    else:
        return []


def astar(matrix, start, end):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    open_list = [(0, start, [])]
    closed_set = set()

    while open_list:
        cost, current, path = heapq.heappop(open_list)
        if current == end:
            return path + [current]

        if current in closed_set:
            continue

        closed_set.add(current)

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]
            if is_valid_move(matrix, new_row, new_col):
                new_cost = cost + 1
                heuristic = abs(new_row - end[0]) + abs(new_col - end[1])
                heapq.heappush(open_list, (new_cost + heuristic, (new_row, new_col), path + [current]))

    return []


def construct_path(parent, start, end):
    path = [end]
    current = end

    while parent[current[0]][current[1]] is not None:
        current = parent[current[0]][current[1]]
        path.append(current)

    return path[::-1]
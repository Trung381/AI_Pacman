import pygame
import sys

# Constants
CELL_SIZE = 30
GRID_COLOR = (0, 0, 0)

# VISITED_COLOR_BFS = (152, 251, 152)
# VISITED_COLOR_DFS = (173, 216, 230)
# VISITED_COLOR_ASTAR = (255, 192, 203)
# WHITE = (225, 225, 225)
# identical_coordinates_color_bfs_dfs = (255, 255, 0)
# identical_coordinates_color_bfs_astar = (128, 0, 128)
# identical_coordinates_color_dfs_astar = (165, 42, 42)
# identical_coordinates_color_all = (139, 10, 80)

VISITED_COLOR_BFS = (173, 216, 230) #xanh dương
VISITED_COLOR_DFS = (255, 255, 152) #vàng
VISITED_COLOR_ASTAR = (255, 192, 203) # đỏ 
WHITE = (225, 225, 225)
identical_coordinates_color_bfs_dfs = (152, 251, 152) # xanh lá
identical_coordinates_color_bfs_astar = (188, 143, 143) # nâu
identical_coordinates_color_dfs_astar = (255, 204, 153) # cam
identical_coordinates_color_all = (209, 204, 255) # tím
FPS = 8

def draw_grid(screen, rows, cols, cell_size):
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)


def draw_maze(screen, matrix, cell_size):
    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            # color = (255, 255, 255) if matrix[row][col] == 0 else (0, 0, 0)
            color = WHITE if matrix[row][col] == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))


def draw_path(screen, path, color, cell_size):
    for row, col in path:
        pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))


def draw_visited(screen, visited, color, cell_size):
    rows, cols = len(visited), len(visited[0])

    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
                pygame.draw.rect(screen, GRID_COLOR, (col * cell_size, row * cell_size, cell_size, cell_size), 1)


def mark_cells_with_identical_coordinates(matrix, visited_bfs, visited_dfs, visited_astar):
    identical_coordinates_bfs_dfs = []
    identical_coordinates_bfs_astar = []
    identical_coordinates_dfs_astar = []
    identical_coordinates_all = []

    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if visited_bfs[row][col] and visited_dfs[row][col]:
                identical_coordinates_bfs_dfs.append((row, col))
            if visited_bfs[row][col] and visited_astar[row][col]:
                identical_coordinates_bfs_astar.append((row, col))
            if visited_dfs[row][col] and visited_astar[row][col]:
                identical_coordinates_dfs_astar.append((row, col))
            if visited_bfs[row][col] and visited_dfs[row][col] and visited_astar[row][col]:
                identical_coordinates_all.append((row, col))

    return identical_coordinates_bfs_dfs, identical_coordinates_bfs_astar, identical_coordinates_dfs_astar, identical_coordinates_all


def draw_identical_coordinates(screen, matrix, coordinates, color, cell_size):
    for row, col in coordinates:
        pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, GRID_COLOR, (col * cell_size, row * cell_size, cell_size, cell_size), 1)
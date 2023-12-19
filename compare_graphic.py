# # compare_graphic.py

# import tkinter as tk
# from tkinter import ttk
# import heapq
# from collections import deque
# import timeit
# from map import matrix, start_position, end_position

# def is_valid_move(matrix, row, col):
#     rows, cols = len(matrix), len(matrix[0])
#     return 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 0

# def manhattan_distance(point1, point2):
#     return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# def bfs_compare(matrix, start, end):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     queue = deque([(start, [])])
#     visited = set()
#     search_length = 0

#     start_time = timeit.default_timer()

#     while queue:
#         current, path = queue.popleft()
#         search_length += 1

#         if current == end:
#             end_time = timeit.default_timer()
#             path_length = len(path) + 1  # +1 to include the last node
#             return path + [current], path_length, search_length, end_time - start_time

#         if current in visited:
#             continue

#         visited.add(current)

#         for direction in directions:
#             new_row, new_col = current[0] + direction[0], current[1] + direction[1]
#             if is_valid_move(matrix, new_row, new_col):
#                 queue.append(((new_row, new_col), path + [current]))

#     return [], 0, search_length, 0

# def dfs_compare(matrix, start, end):
#     visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#     path = []
#     search_length = 0

#     start_time = timeit.default_timer()

#     def dfs_helper(row, col):
#         nonlocal path, search_length
#         if not is_valid_move(matrix, row, col) or visited[row][col]:
#             return None, 0

#         visited[row][col] = True
#         path.append((row, col))
#         search_length += 1

#         if (row, col) == end:
#             end_time = timeit.default_timer()
#             return path, end_time - start_time

#         moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left

#         for move in moves:
#             new_row, new_col = row + move[0], col + move[1]
#             if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#                 result, elapsed_time = dfs_helper(new_row, new_col)
#                 if result is not None:
#                     return result, elapsed_time

#         path.pop()
#         return None, 0

#     start_row, start_col = start
#     result, elapsed_time = dfs_helper(start_row, start_col)

#     if result is not None:
#         path_length = len(result)
#         return result, path_length, search_length, elapsed_time
#     else:
#         return [], 0, search_length, elapsed_time

# def astar_compare(matrix, start, end):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     open_list = [(0, start, [])]
#     closed_set = set()
#     search_length = 0

#     start_time = timeit.default_timer()

#     while open_list:
#         cost, current, path = heapq.heappop(open_list)
#         search_length += 1

#         if current == end:
#             end_time = timeit.default_timer()
#             path_length = len(path) + 1  # +1 to include the last node
#             return path + [current], path_length, search_length, end_time - start_time

#         if current in closed_set:
#             continue

#         closed_set.add(current)

#         for direction in directions:
#             new_row, new_col = current[0] + direction[0], current[1] + direction[1]
#             if is_valid_move(matrix, new_row, new_col):
#                 new_cost = cost + 1
#                 heuristic = manhattan_distance((new_row, new_col), end)
#                 heapq.heappush(open_list, (new_cost + heuristic, (new_row, new_col), path + [current]))

#     return [], 0, search_length, 0

# def create_table(window, data):
#     table = ttk.Treeview(window, columns=("Algorithm", "Path Length", "Search Length", "Time"), show="headings")
#     table.heading("Algorithm", text="Algorithm")
#     table.heading("Path Length", text="Path Length")
#     table.heading("Search Length", text="Search Length")
#     table.heading("Time", text="Time (seconds)")

#     for col in ("Algorithm", "Path Length", "Search Length", "Time"):
#         table.column(col, anchor="center")

#     for row in data:
#         table.insert("", "end", values=row)

#     table.pack(fill="both", expand=True, padx=10, pady=10)

# def close_window(window):
#     window.destroy()

# def show_compare_window(matrix, start_position, end_position):
#     cbfs_path, bfs_path_length, bfs_search_length, bfs_time = bfs_compare(matrix, start_position, end_position)
#     cdfs_path, dfs_path_length, dfs_search_length, dfs_time = dfs_compare(matrix, start_position, end_position)
#     castar_path, astar_path_length, astar_search_length, astar_time = astar_compare(matrix, start_position, end_position)
#     # bfs_path, bfs_path_length, bfs_search_length, bfs_time = bfs_compare(matrix, start_position, end_position)
#     # dfs_path, dfs_path_length, dfs_search_length, dfs_time = dfs_compare(matrix, start_position, end_position)
#     # astar_path, astar_path_length, astar_search_length, astar_time = astar_compare(matrix, start_position, end_position)

#     data = [
#         ("BFS", bfs_path_length, bfs_search_length, bfs_time),
#         ("DFS", dfs_path_length, dfs_search_length, dfs_time),
#         ("A*", astar_path_length, astar_search_length, astar_time),
#     ]

#     window = tk.Tk()
#     window.title("Pathfinding Algorithm Comparison")

#     create_table(window, data)

#     close_button = tk.Button(window, text="Close", command=lambda: close_window(window))
#     close_button.pack(pady=10)

#     window.mainloop()

# if __name__ == "__main__":
#     show_compare_window(matrix, start_position, end_position)



####################################################################################################





# import pygame
# import sys
# import heapq
# from collections import deque
# import timeit
# from map import matrix, start_position, end_position

# # Your existing pathfinding functions

# def is_valid_move(matrix, row, col):
#     rows, cols = len(matrix), len(matrix[0])
#     return 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 0

# def manhattan_distance(point1, point2):
#     return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# def bfs(matrix, start, end):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     queue = deque([(start, [])])
#     visited = set()
#     search_length = 0

#     start_time = timeit.default_timer()

#     while queue:
#         current, path = queue.popleft()
#         search_length += 1

#         if current == end:
#             end_time = timeit.default_timer()
#             path_length = len(path) + 1  # +1 to include the last node
#             return path + [current], path_length, search_length, end_time - start_time

#         if current in visited:
#             continue

#         visited.add(current)

#         for direction in directions:
#             new_row, new_col = current[0] + direction[0], current[1] + direction[1]
#             if is_valid_move(matrix, new_row, new_col):
#                 queue.append(((new_row, new_col), path + [current]))

#     return [], 0, search_length, 0

# def dfs(matrix, start, end):
#     visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#     path = []
#     search_length = 0

#     start_time = timeit.default_timer()

#     def dfs_helper(row, col):
#         nonlocal path, search_length
#         if not is_valid_move(matrix, row, col) or visited[row][col]:
#             return None, 0

#         visited[row][col] = True
#         path.append((row, col))
#         search_length += 1

#         if (row, col) == end:
#             end_time = timeit.default_timer()
#             return path, end_time - start_time

#         moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left

#         for move in moves:
#             new_row, new_col = row + move[0], col + move[1]
#             if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#                 result, elapsed_time = dfs_helper(new_row, new_col)
#                 if result is not None:
#                     return result, elapsed_time

#         path.pop()
#         return None, 0

#     start_row, start_col = start
#     result, elapsed_time = dfs_helper(start_row, start_col)

#     if result is not None:
#         path_length = len(result)
#         return result, path_length, search_length, elapsed_time
#     else:
#         return [], 0, search_length, elapsed_time

# def astar_search(matrix, start, end):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     open_list = [(0, start, [])]
#     closed_set = set()
#     search_length = 0

#     start_time = timeit.default_timer()

#     while open_list:
#         cost, current, path = heapq.heappop(open_list)
#         search_length += 1

#         if current == end:
#             end_time = timeit.default_timer()
#             path_length = len(path) + 1  # +1 to include the last node
#             return path + [current], path_length, search_length, end_time - start_time

#         if current in closed_set:
#             continue

#         closed_set.add(current)

#         for direction in directions:
#             new_row, new_col = current[0] + direction[0], current[1] + direction[1]
#             if is_valid_move(matrix, new_row, new_col):
#                 new_cost = cost + 1
#                 heuristic = manhattan_distance((new_row, new_col), end)
#                 heapq.heappush(open_list, (new_cost + heuristic, (new_row, new_col), path + [current]))

#     return [], 0, search_length, 0


# # Function to draw text on the window
# def draw_text(surface, text, pos, font, color):
#     text_surface = font.render(text, True, color)
#     surface.blit(text_surface, pos)

# # Function to create the Pygame window with the table
# def create_window():
#     pygame.init()
#     window_size = (660, 300)
#     screen = pygame.display.set_mode(window_size)
#     pygame.display.set_caption("Pathfinding Results")

#     # Load background image
#     background_image = pygame.image.load("access/background.png")

#     return screen, background_image

# # Function to display the results table
# def display_results(screen, results):
#     font = pygame.font.Font(None, 24)
#     header_color = (0, 0, 0)  # Change the header color to black
#     row_color = (0, 0, 0)

#     # Header
#     draw_text(screen, "Algorithms", (50, 50), font, header_color)
#     draw_text(screen, "Path Length", (200, 50), font, header_color)
#     draw_text(screen, "Search Length", (350, 50), font, header_color)
#     draw_text(screen, "Time (seconds)", (500, 50), font, header_color)

#     row_height = 50
#     y_position = 100

#     # Display results
#     for algorithm, result in results.items():
#         # Algorithm name
#         draw_text(screen, algorithm, (50, y_position), font, row_color)

#         # Path Length
#         draw_text(screen, str(result['path_length']), (200, y_position), font, row_color)

#         # Search Length
#         draw_text(screen, str(result['search_length']), (350, y_position), font, row_color)

#         # Time
#         draw_text(screen, "{:.6f}".format(result['time']), (500, y_position), font, row_color)

#         y_position += row_height

# # Main function
# def main():
#     screen, background_image = create_window()

#     maze = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
#     [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
#     [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
#     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
# ]

#     start = (0, 0)
#     end = (14, 14)

#     bfs_path, bfs_path_length, bfs_search_length, bfs_time = bfs(maze, start, end)
#     dfs_path, dfs_path_length, dfs_search_length, dfs_time = dfs(maze, start, end)
#     astar_path, astar_path_length, astar_search_length, astar_time = astar_search(maze, start, end)

#     results = {
#         'BFS': {'path_length': bfs_path_length, 'search_length': bfs_search_length, 'time': bfs_time},
#         'DFS': {'path_length': dfs_path_length, 'search_length': dfs_search_length, 'time': dfs_time},
#         'A*': {'path_length': astar_path_length, 'search_length': astar_search_length, 'time': astar_time}
#     }

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Blit the background image onto the screen
#         screen.blit(background_image, (0, 0))

#         # Display results on top of the background image
#         display_results(screen, results)

#         pygame.display.flip()

# if __name__ == "__main__":
#     main()







####################################################################################################





# import pygame
# import sys
# import heapq
# from collections import deque
# import timeit
# from map import *

# # Your existing pathfinding functions

# def is_valid_move(matrix, row, col):
#     rows, cols = len(matrix), len(matrix[0])
#     return 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 0

# def manhattan_distance(point1, point2):
#     return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# def bfs(matrix, start, end):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     queue = deque([(start, [])])
#     visited = set()
#     search_length = 0

#     start_time = timeit.default_timer()

#     while queue:
#         current, path = queue.popleft()
#         search_length += 1

#         if current == end:
#             end_time = timeit.default_timer()
#             path_length = len(path) + 1  # +1 to include the last node
#             return path + [current], path_length, search_length, end_time - start_time

#         if current in visited:
#             continue

#         visited.add(current)

#         for direction in directions:
#             new_row, new_col = current[0] + direction[0], current[1] + direction[1]
#             if is_valid_move(matrix, new_row, new_col):
#                 queue.append(((new_row, new_col), path + [current]))

#     return [], 0, search_length, 0

# def dfs(matrix, start, end):
#     visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#     path = []
#     search_length = 0

#     start_time = timeit.default_timer()

#     def dfs_helper(row, col):
#         nonlocal path, search_length
#         if not is_valid_move(matrix, row, col) or visited[row][col]:
#             return None, 0

#         visited[row][col] = True
#         path.append((row, col))
#         search_length += 1

#         if (row, col) == end:
#             end_time = timeit.default_timer()
#             return path, end_time - start_time

#         moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left

#         for move in moves:
#             new_row, new_col = row + move[0], col + move[1]
#             if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#                 result, elapsed_time = dfs_helper(new_row, new_col)
#                 if result is not None:
#                     return result, elapsed_time

#         path.pop()
#         return None, 0

#     start_row, start_col = start
#     result, elapsed_time = dfs_helper(start_row, start_col)

#     if result is not None:
#         path_length = len(result)
#         return result, path_length, search_length, elapsed_time
#     else:
#         return [], 0, search_length, elapsed_time

# def astar_search(matrix, start, end):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     open_list = [(0, start, [])]
#     closed_set = set()
#     search_length = 0

#     start_time = timeit.default_timer()

#     while open_list:
#         cost, current, path = heapq.heappop(open_list)
#         search_length += 1

#         if current == end:
#             end_time = timeit.default_timer()
#             path_length = len(path) + 1  # +1 to include the last node
#             return path + [current], path_length, search_length, end_time - start_time

#         if current in closed_set:
#             continue

#         closed_set.add(current)

#         for direction in directions:
#             new_row, new_col = current[0] + direction[0], current[1] + direction[1]
#             if is_valid_move(matrix, new_row, new_col):
#                 new_cost = cost + 1
#                 heuristic = manhattan_distance((new_row, new_col), end)
#                 heapq.heappush(open_list, (new_cost + heuristic, (new_row, new_col), path + [current]))

#     return [], 0, search_length, 0

# # Function to draw text on the window
# def draw_text(surface, text, pos, font, color):
#     text_surface = font.render(text, True, color)
#     surface.blit(text_surface, pos)

# # Function to create the Pygame window with the table
# def create_window():
#     pygame.init()
#     window_size = (660, 300)
#     screen = pygame.display.set_mode(window_size)
#     pygame.display.set_caption("Pathfinding Results")

#     # Load background image
#     background_image = pygame.image.load("access/background_c.png")

#     return screen, background_image

# # Function to display the results table
# def display_results(screen, results):
#     font = pygame.font.Font(None, 24)
#     header_color = (0, 0, 0)  # Change the header color to black
#     row_color = (0, 0, 0)

#     # Header
#     draw_text(screen, "Algorithms", (50, 50), font, header_color)
#     draw_text(screen, "Path Length", (200, 50), font, header_color)
#     draw_text(screen, "Search Length", (350, 50), font, header_color)
#     draw_text(screen, "Time (seconds)", (500, 50), font, header_color)

#     row_height = 50
#     y_position = 100

#     # Display results
#     for algorithm, result in results.items():
#         # Algorithm name
#         draw_text(screen, algorithm, (50, y_position), font, row_color)

#         # Path Length
#         draw_text(screen, str(result['path_length']), (200, y_position), font, row_color)

#         # Search Length
#         draw_text(screen, str(result['search_length']), (350, y_position), font, row_color)

#         # Time
#         draw_text(screen, "{:.6f}".format(result['time']), (500, y_position), font, row_color)

#         y_position += row_height

# # Main function
# def show_compare_window(matrix, start_position, end_position):
#     screen, background_image = create_window()

#     bfs_path, bfs_path_length, bfs_search_length, bfs_time = bfs(matrix, start_position, end_position)
#     dfs_path, dfs_path_length, dfs_search_length, dfs_time = dfs(matrix, start_position, end_position)
#     astar_path, astar_path_length, astar_search_length, astar_time = astar_search(matrix, start_position, end_position)

#     results = {
#         'BFS': {'path_length': bfs_path_length, 'search_length': bfs_search_length, 'time': bfs_time},
#         'DFS': {'path_length': dfs_path_length, 'search_length': dfs_search_length, 'time': dfs_time},
#         'A*': {'path_length': astar_path_length, 'search_length': astar_search_length, 'time': astar_time}
#     }

#     button_rect = pygame.Rect(270, 250, 90, 40)  # (x, y, width, height)
#     button_color = (255, 0, 0)  # Red color for the button
#     font = pygame.font.Font(None, 24)
#     button_text = font.render("Close", True, (255, 255, 255))  # White text

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 # Check if the mouse click is within the button area
#                 if button_rect.collidepoint(event.pos):
#                     running = False

#         # Blit the background image onto the screen
#         screen.blit(background_image, (0, 0))

#         # Display results on top of the background image
#         display_results(screen, results)

#         # Draw the close button
#         pygame.draw.rect(screen, button_color, button_rect)
#         screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))  # Adjust text position

#         pygame.display.flip()

#     pygame.quit()
#     sys.exit()


# # if __name__ == "__main__":
# #     show_compare_window(matrix, start_position, end_position)








import pygame
import sys
import heapq
from collections import deque
import timeit
from map import *

# Your existing pathfinding functions

def is_valid_move(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 0

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def bfs(matrix, start, end):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(start, [])])
    visited = set()
    search_length = 0

    start_time = timeit.default_timer()

    while queue:
        current, path = queue.popleft()
        search_length += 1

        if current == end:
            end_time = timeit.default_timer()
            path_length = len(path) + 1  # +1 to include the last node
            return path + [current], path_length, search_length, end_time - start_time

        if current in visited:
            continue

        visited.add(current)

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]
            if is_valid_move(matrix, new_row, new_col):
                queue.append(((new_row, new_col), path + [current]))

    return [], 0, search_length, 0

def dfs(matrix, start, end):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    path = []
    search_length = 0

    start_time = timeit.default_timer()

    def dfs_helper(row, col):
        nonlocal path, search_length
        if not is_valid_move(matrix, row, col) or visited[row][col]:
            return None, 0

        visited[row][col] = True
        path.append((row, col))
        search_length += 1

        if (row, col) == end:
            end_time = timeit.default_timer()
            return path, end_time - start_time

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                result, elapsed_time = dfs_helper(new_row, new_col)
                if result is not None:
                    return result, elapsed_time

        path.pop()
        return None, 0

    start_row, start_col = start
    result, elapsed_time = dfs_helper(start_row, start_col)

    if result is not None:
        path_length = len(result)
        return result, path_length, search_length, elapsed_time
    else:
        return [], 0, search_length, elapsed_time

def astar_search(matrix, start, end):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    open_list = [(0, start, [])]
    closed_set = set()
    search_length = 0

    start_time = timeit.default_timer()

    while open_list:
        cost, current, path = heapq.heappop(open_list)
        search_length += 1

        if current == end:
            end_time = timeit.default_timer()
            path_length = len(path) + 1  # +1 to include the last node
            return path + [current], path_length, search_length, end_time - start_time

        if current in closed_set:
            continue

        closed_set.add(current)

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]
            if is_valid_move(matrix, new_row, new_col):
                new_cost = cost + 1
                heuristic = manhattan_distance((new_row, new_col), end)
                heapq.heappush(open_list, (new_cost + heuristic, (new_row, new_col), path + [current]))

    return [], 0, search_length, 0

# Function to draw text on the window
def draw_text(surface, text, pos, font, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)


# Function to create the Pygame window with the table
def create_window():
    pygame.init()
    window_size = (660, 300)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Pathfinding Results")

    # Load background image and resize
    original_background = pygame.image.load("access/background_c.png")
    background_image = pygame.transform.scale(original_background, window_size)

    return screen, background_image

# Function to display the results table
def display_results(screen, results):
    font = pygame.font.Font(None, 24)
    header_color = (0, 0, 0)  # Change the header color to black
    row_color = (0, 0, 0)

    # Header
    draw_text(screen, "Algorithms", (50, 50), font, header_color)
    draw_text(screen, "Path Length", (200, 50), font, header_color)
    draw_text(screen, "Search Length", (350, 50), font, header_color)
    draw_text(screen, "Time (seconds)", (500, 50), font, header_color)

    row_height = 50
    y_position = 100

    # Display results
    for algorithm, result in results.items():
        # Algorithm name
        draw_text(screen, algorithm, (50, y_position), font, row_color)

        # Path Length
        draw_text(screen, str(result['path_length']), (200, y_position), font, row_color)

        # Search Length
        draw_text(screen, str(result['search_length']), (350, y_position), font, row_color)

        # Time
        draw_text(screen, "{:.6f}".format(result['time']), (500, y_position), font, row_color)

        y_position += row_height

# Main function
def show_compare_window(matrix, start_position, end_position):
    screen, background_image = create_window()

    bfs_path, bfs_path_length, bfs_search_length, bfs_time = bfs(matrix, start_position, end_position)
    dfs_path, dfs_path_length, dfs_search_length, dfs_time = dfs(matrix, start_position, end_position)
    astar_path, astar_path_length, astar_search_length, astar_time = astar_search(matrix, start_position, end_position)

    results = {
        'BFS': {'path_length': bfs_path_length, 'search_length': bfs_search_length, 'time': bfs_time},
        'DFS': {'path_length': dfs_path_length, 'search_length': dfs_search_length, 'time': dfs_time},
        'A*': {'path_length': astar_path_length, 'search_length': astar_search_length, 'time': astar_time}
    }

    button_rect = pygame.Rect(270, 250, 90, 40)  # (x, y, width, height)
    button_color = (255, 0, 0)  # Red color for the button
    font = pygame.font.Font(None, 24)
    button_text = font.render("Close", True, (255, 255, 255))  # White text

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the mouse click is within the button area
                if button_rect.collidepoint(event.pos):
                    running = False

        # Blit the resized background image onto the screen
        screen.blit(background_image, (0, 0))

        # Display results on top of the background image
        display_results(screen, results)

        # Draw the close button
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))  # Adjust text position

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# if __name__ == "__main__":
#     show_compare_window(matrix, start_position, end_position)

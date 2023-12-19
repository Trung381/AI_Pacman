import pygame
import sys
from map import *
from searching import bfs, dfs, astar
from drawing import *

# Constants
CELL_SIZE = 20
GRID_COLOR = (0, 0, 0)

VISITED_COLOR_BFS = (0, 245, 255)  # xanh dương
VISITED_COLOR_DFS = (192, 255, 62)  # vàng
VISITED_COLOR_ASTAR = (255, 106, 106)  # đỏ

WHITE = (225, 225, 225)

identical_coordinates_color_bfs_dfs = (191, 62, 225)  # xanh lá
identical_coordinates_color_bfs_astar = (255, 20, 147)  # nâu
identical_coordinates_color_dfs_astar = (132, 112, 255)  # cam
identical_coordinates_color_all = (25, 25, 112)  # tím

FPS = 15


def run_main(matrix, start_position, end_position):
    pygame.init()

    bfs_path = bfs(matrix, start_position, end_position)
    dfs_path = dfs(matrix, start_position, end_position)
    astar_path = astar(matrix, start_position, end_position)

    if not bfs_path or not dfs_path or not astar_path:
        show_path_not_found_message()
        pygame.quit()
        sys.exit()

    screen_size = (len(matrix[0]) * CELL_SIZE, len(matrix) * CELL_SIZE)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Pacman - no way to escape")

    character_bfs = pygame.image.load("access/bfs.png")
    character_dfs = pygame.image.load("access/dfs.png")
    character_astar = pygame.image.load("access/astar.png")
    character_pacman = pygame.image.load("access/pacman.png")

    character_bfs = pygame.transform.scale(character_bfs, (CELL_SIZE, CELL_SIZE))
    character_dfs = pygame.transform.scale(character_dfs, (CELL_SIZE, CELL_SIZE))
    character_astar = pygame.transform.scale(character_astar, (CELL_SIZE, CELL_SIZE))
    character_pacman = pygame.transform.scale(character_pacman, (CELL_SIZE, CELL_SIZE))

    character_positions = {
        'bfs': start_position,
        'dfs': start_position,
        'astar': start_position,
        'pacman': end_position,
    }

    move_characters = False

    visited_bfs = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    visited_dfs = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    visited_astar = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    move_characters = True

        screen.fill(WHITE)
        draw_maze(screen, matrix, CELL_SIZE)

        draw_path(screen, bfs_path, WHITE, CELL_SIZE)
        draw_path(screen, dfs_path, WHITE, CELL_SIZE)
        draw_path(screen, astar_path, WHITE, CELL_SIZE)

        draw_grid(screen, len(matrix), len(matrix[0]), CELL_SIZE)

        if move_characters:
            draw_visited(screen, visited_bfs, VISITED_COLOR_BFS, CELL_SIZE)
            draw_visited(screen, visited_dfs, VISITED_COLOR_DFS, CELL_SIZE)
            draw_visited(screen, visited_astar, VISITED_COLOR_ASTAR, CELL_SIZE)

            identical_coordinates_bfs_dfs, identical_coordinates_bfs_astar, identical_coordinates_dfs_astar, identical_coordinates_all = mark_cells_with_identical_coordinates(
                matrix, visited_bfs, visited_dfs, visited_astar)

            draw_identical_coordinates(screen, matrix, identical_coordinates_bfs_dfs,
                                       identical_coordinates_color_bfs_dfs,
                                       CELL_SIZE)  # Yellow
            draw_identical_coordinates(screen, matrix, identical_coordinates_bfs_astar,
                                       identical_coordinates_color_bfs_astar,
                                       CELL_SIZE)  # Purple
            draw_identical_coordinates(screen, matrix, identical_coordinates_dfs_astar,
                                       identical_coordinates_color_dfs_astar,
                                       CELL_SIZE)  # Brown
            draw_identical_coordinates(screen, matrix, identical_coordinates_all, identical_coordinates_color_all,
                                       CELL_SIZE)  # Dark Pink

            if len(bfs_path) > 1:
                visited_bfs[character_positions['bfs'][0]][character_positions['bfs'][1]] = True
                character_positions['bfs'] = bfs_path[1]
                bfs_path = bfs_path[1:]

            if len(dfs_path) > 1:
                visited_dfs[character_positions['dfs'][0]][character_positions['dfs'][1]] = True
                character_positions['dfs'] = dfs_path[1]
                dfs_path = dfs_path[1:]

            if len(astar_path) > 1:
                visited_astar[character_positions['astar'][0]][character_positions['astar'][1]] = True
                character_positions['astar'] = astar_path[1]
                astar_path = astar_path[1:]

        screen.blit(character_bfs,
                    (character_positions['bfs'][1] * CELL_SIZE, character_positions['bfs'][0] * CELL_SIZE))
        screen.blit(character_dfs,
                    (character_positions['dfs'][1] * CELL_SIZE, character_positions['dfs'][0] * CELL_SIZE))
        screen.blit(character_pacman,
                    (character_positions['pacman'][1] * CELL_SIZE, character_positions['pacman'][0] * CELL_SIZE))
        screen.blit(character_astar,
                    (character_positions['astar'][1] * CELL_SIZE, character_positions['astar'][0] * CELL_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def show_path_not_found_message():
    pygame.init()

    screen_size = (400, 100)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Path Not Found")

    font = pygame.font.Font(None, 36)

    text = font.render("Path not found!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()


# if __name__ == "__main__":
#     play(matrix, start_position, end_position)



# #main.py

# from compare_graphic import show_compare_window
# from map import *
# from searching import bfs, dfs, astar
# from drawing import *

# # Constants
# CELL_SIZE = 20
# GRID_COLOR = (0, 0, 0)

# VISITED_COLOR_BFS = (0, 245, 255) #xanh dương
# VISITED_COLOR_DFS = (192, 255, 62) #vàng
# VISITED_COLOR_ASTAR = (255, 106, 106) # đỏ 

# WHITE = (225, 225, 225)

# identical_coordinates_color_bfs_dfs = (191, 62, 225) # xanh lá
# identical_coordinates_color_bfs_astar = (255, 20, 147) # nâu
# identical_coordinates_color_dfs_astar = (132, 112, 255) # cam
# identical_coordinates_color_all = (25, 25, 112) # tím

# FPS = 25


# def play(matrix, start_position, end_position):
#     pygame.init()

#     bfs_path = bfs(matrix, start_position, end_position)
#     dfs_path = dfs(matrix, start_position, end_position)
#     astar_path = astar(matrix, start_position, end_position)

#     if not bfs_path or not dfs_path or not astar_path:
#         print("No path found.")
#         sys.exit()

#     screen_size = (len(matrix[0]) * CELL_SIZE, len(matrix) * CELL_SIZE)
#     screen = pygame.display.set_mode(screen_size)
#     pygame.display.set_caption("Pacman - no way to escape")

#     character_bfs = pygame.image.load("access/bfs.png")
#     character_dfs = pygame.image.load("access/dfs.png")
#     character_astar = pygame.image.load("access/astar.png")
#     character_pacman = pygame.image.load("access/pacman.png")


#     character_bfs = pygame.transform.scale(character_bfs, (CELL_SIZE, CELL_SIZE))
#     character_dfs = pygame.transform.scale(character_dfs, (CELL_SIZE, CELL_SIZE))
#     character_astar = pygame.transform.scale(character_astar, (CELL_SIZE, CELL_SIZE))
#     character_pacman = pygame.transform.scale(character_pacman, (CELL_SIZE, CELL_SIZE))

#     character_positions = {
#         'bfs': start_position,
#         'dfs': start_position,
#         'astar': start_position,
#         'pacman': end_position,
#     }

#     move_characters = False

#     visited_bfs = [[False] * len(matrix[0]) for _ in range(len(matrix))]
#     visited_dfs = [[False] * len(matrix[0]) for _ in range(len(matrix))]
#     visited_astar = [[False] * len(matrix[0]) for _ in range(len(matrix))]

#     running = True
#     clock = pygame.time.Clock()

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     move_characters = True

#         screen.fill(WHITE)
#         draw_maze(screen, matrix, CELL_SIZE)

#         draw_path(screen, bfs_path, WHITE, CELL_SIZE)
#         draw_path(screen, dfs_path, WHITE, CELL_SIZE)
#         draw_path(screen, astar_path, WHITE, CELL_SIZE)

#         draw_grid(screen, len(matrix), len(matrix[0]), CELL_SIZE)

#         if move_characters:
#             draw_visited(screen, visited_bfs, VISITED_COLOR_BFS, CELL_SIZE)
#             draw_visited(screen, visited_dfs, VISITED_COLOR_DFS, CELL_SIZE)
#             draw_visited(screen, visited_astar, VISITED_COLOR_ASTAR, CELL_SIZE)

#             identical_coordinates_bfs_dfs, identical_coordinates_bfs_astar, identical_coordinates_dfs_astar, identical_coordinates_all = mark_cells_with_identical_coordinates(
#                 matrix, visited_bfs, visited_dfs, visited_astar)

#             draw_identical_coordinates(screen, matrix, identical_coordinates_bfs_dfs, identical_coordinates_color_bfs_dfs,
#                                        CELL_SIZE)  # Yellow
#             draw_identical_coordinates(screen, matrix, identical_coordinates_bfs_astar, identical_coordinates_color_bfs_astar,
#                                        CELL_SIZE)  # Purple
#             draw_identical_coordinates(screen, matrix, identical_coordinates_dfs_astar, identical_coordinates_color_dfs_astar,
#                                        CELL_SIZE)  # Brown
#             draw_identical_coordinates(screen, matrix, identical_coordinates_all, identical_coordinates_color_all,
#                                        CELL_SIZE)  # Dark Pink

#             if len(bfs_path) > 1:
#                 visited_bfs[character_positions['bfs'][0]][character_positions['bfs'][1]] = True
#                 character_positions['bfs'] = bfs_path[1]
#                 bfs_path = bfs_path[1:]

#             if len(dfs_path) > 1:
#                 visited_dfs[character_positions['dfs'][0]][character_positions['dfs'][1]] = True
#                 character_positions['dfs'] = dfs_path[1]
#                 dfs_path = dfs_path[1:]

#             if len(astar_path) > 1:
#                 visited_astar[character_positions['astar'][0]][character_positions['astar'][1]] = True
#                 character_positions['astar'] = astar_path[1]
#                 astar_path = astar_path[1:]

#         screen.blit(character_bfs,
#                     (character_positions['bfs'][1] * CELL_SIZE, character_positions['bfs'][0] * CELL_SIZE))
#         screen.blit(character_dfs,
#                     (character_positions['dfs'][1] * CELL_SIZE, character_positions['dfs'][0] * CELL_SIZE))
#         screen.blit(character_pacman, 
#                     (character_positions['pacman'][1] * CELL_SIZE, character_positions['pacman'][0] * CELL_SIZE))
#         screen.blit(character_astar,
#                     (character_positions['astar'][1] * CELL_SIZE, character_positions['astar'][0] * CELL_SIZE))

#         pygame.display.flip()
#         clock.tick(FPS)
    
#     pygame.quit()

# if __name__ == "__main__":
#     play(matrix, start_position, end_position)





##################################################################################
# # import pygame
# import pygame_gui
# import map  # assuming map.py contains matrices a, b, c, d, e

# pygame.init()
# pygame.display.set_caption("Pacman - AI Project")

# # Create Pygame window
# window_size = (600, 400)
# screen = pygame.display.set_mode(window_size)
# manager = pygame_gui.UIManager(window_size)
# background_menu_image = pygame.image.load("access/background.png")

# # Create UI elements
# play_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((350, 200), (200, 50)),
#     text='Play',
#     manager=manager
# )

# testing_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((350, 300), (200, 50)),
#     text='Testing',
#     manager=manager
# )

# # Create buttons for each matrix
# matrix_buttons = {}
# matrix_names = ['a', 'b', 'c', 'd', 'e']
# button_y = 100

# for matrix_name in matrix_names:
#     matrix_buttons[matrix_name] = pygame_gui.elements.UIButton(
#         relative_rect=pygame.Rect((50, button_y), (200, 50)),
#         text=f'Select {matrix_name}',
#         manager=manager
#     )
#     button_y += 60

# selected_matrix = None  # Variable to store the selected matrix

# running = True
# clock = pygame.time.Clock()

# while running:
#     time_delta = clock.tick(60) / 1000.0

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.USEREVENT:
#             if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
#                 if event.ui_element == play_button:
#                     if selected_matrix:
#                         play(selected_matrix)
#                 elif event.ui_element == testing_button:
#                     if selected_matrix:
#                         show_compare_window(selected_matrix, start_position, end_position)
#                 else:
#                     # Check if a matrix button is pressed
#                     for matrix_name in matrix_names:
#                         if event.ui_element == matrix_buttons[matrix_name]:
#                             selected_matrix = getattr(map, matrix_name)

#         manager.process_events(event)

#     manager.update(time_delta)

#     screen.fill(WHITE)
#     manager.draw_ui(screen)

#     pygame.display.flip()

# pygame.quit()


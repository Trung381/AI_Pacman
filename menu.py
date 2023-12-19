# import pygame
# import pygame_gui
# from map import *
# from main import *
# from compare_graphic import *

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Pacman - AI Project & Matrix Viewer")

# # Set up fonts
# font = pygame.font.Font(None, 36)

# # Define colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Define matrices
# matrices = {'a': a, 'b': b, 'c': c, 'd': d}
# current_matrix = None

# # Create UI elements
# manager = pygame_gui.UIManager((screen_width, screen_height))

# play_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((50, 300), (200, 50)),
#     text='Play',
#     manager=manager
# )

# testing_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((350, 300), (200, 50)),
#     text='Testing',
#     manager=manager
# )

# # Main game loop
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
#                     if current_matrix is not None:  # Ensure current_matrix is not None
#                         play(matrices[current_matrix], start_position, end_position)   #####
#                 elif event.ui_element == testing_button:
#                     if current_matrix is not None:  # Ensure current_matrix is not None
#                         show_compare_window(matrices[current_matrix], start_position, end_position)  ##### 
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 x, y = event.pos
#                 # Check if a button is clicked
#                 for matrix_name, matrix in matrices.items():
#                     button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 50, 100, 50)
#                     if button_rect.collidepoint(x, y):
#                         current_matrix = matrix_name
#         manager.process_events(event)
#     manager.update(time_delta)
#     screen.fill(white)
#     # Draw buttons
#     for matrix_name, matrix in matrices.items():
#         button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 50, 100, 50)
#         pygame.draw.rect(screen, black, button_rect, 2)
#         text = font.render(matrix_name, True, black)
#         screen.blit(text, (button_rect.centerx - text.get_width() // 2, button_rect.centery - text.get_height() // 2))
#     manager.draw_ui(screen)
#     pygame.display.flip()

# # Print the selected matrix to the console
# if current_matrix is not None:
#     print(f"Matrix {current_matrix}:")
#     print(matrices[current_matrix])

# # Quit Pygame
# pygame.quit()




######################################################################
# import pygame
# import pygame_gui
# from map import *
# from main import *
# from compare_graphic import *
# import threading

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Pacman - AI Project & Matrix Viewer")

# # Set up fonts
# font = pygame.font.Font(None, 36)

# # Define colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Define matrices
# matrices = {'a': a, 'b': b, 'c': c, 'd': d}
# current_matrix = None

# # Create UI elements
# manager = pygame_gui.UIManager((screen_width, screen_height))

# play_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((50, 300), (200, 50)),
#     text='Play',
#     manager=manager
# )

# testing_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((350, 300), (200, 50)),
#     text='Testing',
#     manager=manager
# )

# def play_wrapper():
#     if current_matrix is not None:
#         play(matrices[current_matrix], start_position, end_position)

# def compare_window_wrapper():
#     if current_matrix is not None:
#         show_compare_window(matrices[current_matrix], start_position, end_position)

# # Main game loop
# running = True
# clock = pygame.time.Clock()

# while running:
#     time_delta = clock.tick(60) / 1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.USEREVENT:
#             if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
#                 if event.ui_element == play_button:
#                     threading.Thread(target=play_wrapper).start()
#                 elif event.ui_element == testing_button:
#                     threading.Thread(target=compare_window_wrapper).start()

#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 x, y = event.pos
#                 for matrix_name, matrix in matrices.items():
#                     button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 50, 100, 50)
#                     if button_rect.collidepoint(x, y):
#                         current_matrix = matrix_name

#         manager.process_events(event)

#     manager.update(time_delta)
#     screen.fill(white)

#     # Draw buttons
#     for matrix_name, matrix in matrices.items():
#         button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 50, 100, 50)
#         pygame.draw.rect(screen, black, button_rect, 2)
#         text = font.render(matrix_name, True, black)
#         screen.blit(text, (button_rect.centerx - text.get_width() // 2, button_rect.centery - text.get_height() // 2))

#     manager.draw_ui(screen)
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()

#############################################################################################


# import pygame
# import pygame_gui
# from map import *
# from main import *
# from compare_graphic import *

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# screen_width, screen_height = 660, 310
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Pacman - AI Project & Matrix Viewer")

# # Set up fonts
# font = pygame.font.Font(None, 36)

# # Define colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Define matrices
# matrices = {'a': a, 'b': b, 'c': c, 'd': d}
# current_matrix = None

# # Create UI elements
# manager = pygame_gui.UIManager((screen_width, screen_height))

# play_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((75, 220), (200, 50)),
#     text='Play',
#     manager=manager
# )

# testing_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((375, 220), (200, 50)),
#     text='Testing',
#     manager=manager
# )

# # Main game loop
# running = True
# clock = pygame.time.Clock()

# # def play(matrix, start, end):
# #     # Your play function code here
# #     print(f"Executing play function with matrix {matrix}")

# # def show_compare_window(matrix, start, end):
# #     # Your show_compare_window function code here
# #     print(f"Executing show_compare_window function with matrix {matrix}")

# while running:
#     time_delta = clock.tick(60) / 1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.USEREVENT:
#             if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
#                 if event.ui_element == play_button:
#                     if current_matrix is not None:
#                         # Execute play function and wait for it to return
#                         play(matrices[current_matrix], start_position, end_position)
#                 elif event.ui_element == testing_button:
#                     if current_matrix is not None:
#                         # Execute show_compare_window function and wait for it to return
#                         show_compare_window(matrices[current_matrix], start_position, end_position)
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 x, y = event.pos
#                 for matrix_name, matrix in matrices.items():
#                     button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 50, 100, 50)
#                     if button_rect.collidepoint(x, y):
#                         current_matrix = matrix_name
#         manager.process_events(event)

#     manager.update(time_delta)
#     screen.fill(white)
    
#     # Draw buttons
#     for matrix_name, matrix in matrices.items():
#         button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 50, 100, 50)
#         pygame.draw.rect(screen, black, button_rect, 2)
#         text = font.render(matrix_name, True, black)
#         screen.blit(text, (button_rect.centerx - text.get_width() // 2, button_rect.centery - text.get_height() // 2))

#     manager.draw_ui(screen)
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()

###########################################################################################

import pygame
import pygame_gui
from map import *
from main import *
from compare_graphic import *

pygame.init()

screen_width, screen_height = 660, 310
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman - No way to escape")

font = pygame.font.Font(None, 36)

original_background = pygame.image.load("access/background3.png")
background_image = pygame.transform.scale(original_background, (screen_width, screen_height))
background_rect = background_image.get_rect()

white = (255, 255, 255)
black = (0, 0, 0)

matrices = {'a': a, 'b': b, 'c': c, 'd': d}
current_matrix = None

manager = pygame_gui.UIManager((screen_width, screen_height))

play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((75, 230), (200, 50)),
    text='Run',
    manager=manager
)

testing_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((375, 230), (200, 50)),
    text='Testing',
    manager=manager
)

running = True
clock = pygame.time.Clock()

while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    if current_matrix is not None:
                        run_main(matrices[current_matrix], start_position, end_position)
                elif event.ui_element == testing_button:
                    if current_matrix is not None:
                        show_compare_window(matrices[current_matrix], start_position, end_position)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for matrix_name, matrix in matrices.items():
                    button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 50, 100, 50)
                    if button_rect.collidepoint(x, y):
                        current_matrix = matrix_name
        manager.process_events(event)

    manager.update(time_delta)
    
    screen.blit(background_image, background_rect)
    
    for matrix_name, matrix in matrices.items():
        button_rect = pygame.Rect(50 + 150 * list(matrices.keys()).index(matrix_name), 30, 100, 50)
        pygame.draw.rect(screen, white, button_rect, 2)
        text = font.render(matrix_name, True, white)
        screen.blit(text, (button_rect.centerx - text.get_width() // 2, button_rect.centery - text.get_height() // 2))

    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()

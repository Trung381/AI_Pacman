# import pygame
# import sys
# # from map import get_matrix  # Assuming get_matrix is a function in map.py
# from map import *  # Assuming get_matrix is a function in map.py
# from compare_graphic import show_compare_window  # Assuming these functions exist in your code
# from main import play

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 400, 300
# FPS = 30
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Set up the display
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Menu")

# # Fonts
# font = pygame.font.Font(None, 36)

# # Button class
# class Button(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height, text, action=None, params=None):
#         super().__init__()
#         self.image = pygame.Surface((width, height))
#         self.rect = self.image.get_rect()
#         self.rect.x, self.rect.y = x, y
#         self.text = text
#         self.action = action
#         self.params = params

#     def draw(self):
#         pygame.draw.rect(screen, WHITE, self.rect)
#         pygame.draw.rect(screen, BLACK, self.rect, 2)
#         self.draw_text()

#     def draw_text(self):
#         text_surface = font.render(self.text, True, BLACK)
#         text_rect = text_surface.get_rect(center=self.rect.center)
#         screen.blit(text_surface, text_rect)

# # Create buttons
# run_button = Button(50, 100, 100, 50, "Run", action=play)
# test_button = Button(250, 100, 100, 50, "Testing", action=show_compare_window)

# buttons = pygame.sprite.Group(run_button, test_button)

# # Main loop
# running = True
# selected_matrix = None

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 # Check if a button is clicked
#                 for button in buttons:
#                     if button.rect.collidepoint(event.pos):
#                         if button.action:
#                             if button.params:
#                                 button.action(*button.params)
#                             else:
#                                 button.action()
                        
#     # Draw buttons
#     screen.fill(BLACK)
#     buttons.draw(screen)
    
#     # Check if a matrix is selected before running
#     if selected_matrix is None:
#         text_surface = font.render("Select a matrix!", True, WHITE)
#         text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
#         screen.blit(text_surface, text_rect)
#     else:
#         text_surface = font.render(f"Selected Matrix: {selected_matrix}", True, WHITE)
#         text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
#         screen.blit(text_surface, text_rect)

#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# sys.exit()














import pygame
from map import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Matrix Viewer")

# Set up fonts
font = pygame.font.Font(None, 36)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define matrices
matrices = {'matrix' : matrix ,'a': a, 'b': b, 'c': c, 'd': d}
current_matrix = None

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                # Check if a button is clicked
                for matrix_name, matrix in matrices.items():
                    button_rect = pygame.Rect(50, 50 + 100 * list(matrices.keys()).index(matrix_name), 100, 50)
                    if button_rect.collidepoint(x, y):
                        current_matrix = matrix_name

    # Draw the screen
    screen.fill(white)

    # Draw buttons
    for matrix_name, matrix in matrices.items():
        button_rect = pygame.Rect(50, 50 + 100 * list(matrices.keys()).index(matrix_name), 100, 50)
        pygame.draw.rect(screen, black, button_rect, 2)
        text = font.render(matrix_name, True, black)
        screen.blit(text, (button_rect.centerx - text.get_width() // 2, button_rect.centery - text.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Print the selected matrix to the console
if current_matrix is not None:
    print(f"Matrix {current_matrix}:")
    print(matrices[current_matrix])

# Quit Pygame
pygame.quit()









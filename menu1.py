# menu1.py
import pygame
import pygame_gui
from map import *
from main import *
from compare_graphic import *


pygame.init()
pygame.display.set_caption("Pacman - AI Project")

# Create Pygame window
window_size = (600, 400)
screen = pygame.display.set_mode(window_size)
manager = pygame_gui.UIManager(window_size)
# background_menu_image = pygame.image.load("access/background.png")

# Create UI elements
play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((50, 300), (200, 50)),
    text='Play',
    manager=manager
)

testing_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 300), (200, 50)),
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
                    play(matrix, start_position, end_position)
                elif event.ui_element == testing_button:
                    show_compare_window(matrix, start_position, end_position)

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill(WHITE)
    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()

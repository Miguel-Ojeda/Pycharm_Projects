# Animation example
# Shows example of SimpleAnimation object
# 1 - Import library
import pygame
from pygame.locals import *
import sys
import pygwidgets
# from simple_animation import *
from simple_sprite_sheet_animation import Simple_Sprite_Sheet_Animation
# 2 Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: images(s), sound(s), etc.
file_numbers_compuesto = 'images_simple_sprite_animation/numbers.png'
file_agua_compuesto = 'images_simple_sprite_animation/water_003.png'

# 5 - Initialize variables
numbers_animation = Simple_Sprite_Sheet_Animation(window, (22, 140), file_numbers_compuesto, 14, 64, 64, .2)
water_animation= Simple_Sprite_Sheet_Animation(window, (400, 140), file_agua_compuesto, 50, 192, 192, .05)

play_button = pygwidgets.TextButton(window, (20, 240), "Play")

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if play_button.handleEvent(event):
            numbers_animation.play()
            water_animation.play()
    # 8 - Do any "per frame" actions
    numbers_animation.update()
    water_animation.update()
    # 9 - Clear the window
    window.fill(BGCOLOR)
    # 10 - Draw all window elements
    numbers_animation.draw()
    water_animation.draw()
    play_button.draw()
    # 11 - Update the window
    pygame.display.update()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)   # make pygame wait
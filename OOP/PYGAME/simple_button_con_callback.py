import sys
import pygame, pygame.event
from pygame.locals import *


class SimpleButton:

    # Posibles estados....
    STATE_IDLE = 'idle'  # button is up, mouse not over button
    STATE_ARMED = 'armed'  # button is down, mouse over button
    STATE_DISARMED = 'disarmed'  # clicked down on button, rolled

    def __init__(self, window: pygame.Surface, posicion, file_button_up, file_button_down, callback_function=None):
        self.window = window
        self.image_up = pygame.image.load(file_button_up)
        self.image_down = pygame.image.load(file_button_down)
        self.rect= self.image_up.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.function_if_clic = callback_function

        # Inicialmente sin activar....
        self.estado = SimpleButton.STATE_IDLE

    def draw(self):
        if self.estado == SimpleButton.STATE_ARMED:
            self.window.blit(self.image_down, self.rect)
        else: # casos DISARMED o IDLE....
            self.window.blit(self.image_up, self.rect)


    def handle_events(self, event: pygame.event.Event):
        # This method will return True if user clicks the button / Normally returns False.
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        colision = self.rect.collidepoint(event.pos)

        if self.estado == SimpleButton.STATE_IDLE:
            if (event.type == MOUSEBUTTONDOWN) and colision:
                self.estado = SimpleButton.STATE_ARMED

        elif self.estado == SimpleButton.STATE_ARMED:
            if (event.type == MOUSEBUTTONUP) and colision:
                self.estado = SimpleButton.STATE_IDLE
                if self.function_if_clic:
                    self.function_if_clic()
                return True  # clicked!

            if (event.type == MOUSEMOTION) and (not colision):
                self.estado = SimpleButton.STATE_DISARMED

        elif self.estado == SimpleButton.STATE_DISARMED:
            if colision:
                self.estado = SimpleButton.STATE_ARMED
            elif event.type == MOUSEBUTTONUP:
                self.estado = SimpleButton.STATE_IDLE

        return False

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if self.rect_up.collidepoint(event.pos):
        #         self.estado = SimpleButton.STATE_ARMED
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     self.estado = SimpleButton.STATE_IDLE



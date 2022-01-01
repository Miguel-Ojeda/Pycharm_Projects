# class Balloon_Manager
import pygame
import random
from pygame.locals import *
import pygwidgets
from constants import *
from balloon import *

class Balloon_Manager:
    def __init__(self, window, max_width, max_height):
        self.window = window
        self.max_width = max_width
        self.max_height = max_height

    def start(self):
        self.balloon_list = []
        self.count_popped = 0
        self.count_missed = 0
        self.score = 0

        for balloon_number in range(N_BALLOONS):
            # Random_Balloon_Class = random.choice(Balloon_Small, Balloon_Medium, Balloon_Large)
            clase_de_globo = Balloon_Medium
            globo = clase_de_globo(self.window, self.max_width, self.max_height, balloon_number)
            self.balloon_list.append(globo)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # Go 'reversed' so topmost balloon gets popped
            for globo in reversed(self.balloon_list):
                was_hit, n_points = globo.clicked_inside(event.pos)
                if was_hit:
                    if n_points > 0:  # remove this balloon ¿¿Por qué hay que comprobar los puntos???
                        self.balloon_list.remove(globo)
                        self.count_popped += 1
                        self.score += n_points
                return  # no need to check others

    def update(self):
        for globo in self.balloon_list:
            status = globo.update()
            # Si nos dice que ya se ha ido por arriba el globo pues nada... habrá que quitarlo
            if status == BALLOON_MISSED:
                self.balloon_list.remove(globo)
                self.count_missed += 1

    def get_score(self):
        return self.score

    def get_count_popped(self):
        return self.count_popped

    def get_count_missed(self):
        return self.count_missed

    def draw(self):
        for globo in self.balloon_list:
            globo.draw()
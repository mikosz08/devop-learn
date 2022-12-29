import pygame

from gui.game_settings import *


class Text():

    def __init__(self, text, size, color, tag="") -> None:
        self.surface = self.create_button_surface(text, size, color)
        self.rect = self.surface.get_rect()
        self.tag = tag

    def create_button_surface(self, text, size, color):
        font = pygame.font.SysFont(TEXT_FONT_CONSOLAS, size)
        antialias = True if (size > ANTIALIASING_THRESHOLD) else False
        surface = font.render(text, antialias, color)
        return surface

    def draw_centered(self, draw_surface, cords):
        self.rect.center = cords
        draw_surface.blit(self.surface, self.rect)
        return self

    def draw(self, draw_surface, cords):
        self.rect = cords
        draw_surface.blit(self.surface, self.rect)
        return self

    def __str__(self) -> str:
        return f"<surface: {self.surface}>, <rec: {self.rect}>, <tag: {self.tag}>"

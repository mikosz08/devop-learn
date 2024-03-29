import pygame
from gui.game_settings import *


class Text():
    def __init__(self, text, size, color) -> None:
        self.raw_text = text
        self.surface = self.create_text_surface(text, size, color)
        self.rect = self.surface.get_rect()

    def create_text_surface(self, text, size, color):
        font = pygame.font.SysFont(TEXT_FONT_CONSOLAS, size)
        antialias = True if (size > ANTIALIASING_THRESHOLD) else False
        text_surface = font.render(text, antialias, color)
        return text_surface

    def draw(self, draw_surface, cords):
        self.rect = cords
        draw_surface.blit(self.surface, self.rect)
        return self

    def get_text(self):
        return self.raw_text

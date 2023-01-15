from gui.Text import Text


class Button():

    def __init__(self, text, size, color, type) -> None:
        self.text = Text(text, size, color)
        self.surface = self.text.surface
        self.rect = self.text.rect
        self.button_type = type

    def draw_centered(self, draw_surface, cords):
        self.text.rect.center = cords
        draw_surface.blit(self.text.surface, self.text.rect)
        return self

    def draw(self, draw_surface, cords):
        self.rect = cords
        draw_surface.blit(self.surface, self.rect)
        return self

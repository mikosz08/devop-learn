import pygame

class Gui():

    WINDOW = pygame.display
    FPS = int
    clock = pygame.time.Clock()
    
    def __init__(self, width, height, title, fps) -> None:
        self.WINDOW.set_mode((width, height))
        self.FPS = fps
        pygame.display.set_caption(title)
        self.main_loop()

    def tick(self):
         self.clock.tick(self.FPS)

    def main_loop(self):
        running = True
        while (running):
            self.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

    


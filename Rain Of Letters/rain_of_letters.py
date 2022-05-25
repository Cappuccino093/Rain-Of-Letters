from pygame.locals import *;
from pygame import Surface;
from pygame.font import Font, SysFont;
import pygame;

class RainOfLetters:
    # Window
    main_surface: Surface;
    surface_caption: str = "Rain of Letters"
    surface_size: tuple[int, int] = (800, 600);

    # Font
    font: Font;
    font_name: str = "Seoge UI Variable";
    font_size: int = 33;
    
    # Color
    primary_color: tuple[int, int, int] = (79, 107, 237);

    def __init__(self):
        pygame.font.init();
        self.font = SysFont(self.font_name, self.font_size);

    def start(self):
        pygame.init();
        pygame.display.set_mode(self.surface_size);
        pygame.display.set_caption(self.surface_caption);

        self.main_surface = pygame.display.get_surface();

        loop = True;
        while (loop):
            
            letterSurface = self.font.render("A", 1, self.primary_color);
            self.main_surface.blit(letterSurface, (0, 0));
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False;

            pygame.display.flip();




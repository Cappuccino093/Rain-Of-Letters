import pygame;
from pygame.locals import *;
from pygame import Surface;
from pygame.font import Font, SysFont;
from letter import Letter;

class RainOfLetters:
    # Window
    __main_surface: Surface;
    __surface_caption: str = "Rain of Letters"
    __surface_size: tuple[int, int] = (800, 600);

    # Flag
    __running = True;

    # Font
    __font: Font;
    __font_name: str = "Seoge UI Variable";
    __font_size: int = 30;
    
    # Color
    __primary_color: tuple[int, int, int] = (79, 107, 237);
    __background_color: tuple[int, int, int] = (32, 31, 30);

    # Letters
    __predefined_letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    __current_letter: Letter;

    # Clock
    __clock = pygame.time.Clock();
    __framerate = 60;
    __frame: int = 0;

    @classmethod
    def __init__(self):
        pygame.font.init();
        self.__font = SysFont(self.__font_name, self.__font_size);

    @classmethod
    def start(self):
        pygame.init();
        pygame.display.set_mode(self.__surface_size);
        pygame.display.set_caption(self.__surface_caption);

        self.__main_surface = pygame.display.get_surface();

        letter = Letter(self.__font, self.__predefined_letters, self.__primary_color);
        self.__current_letter = letter;

        while (self.__running):
            self.__clock.tick(self.__framerate);
            self.__frame += 1;

            if ((self.__frame % 60) == 0):
                self.__frame = 0;
                self.__print_letter();
                self.__check_events();
                pygame.display.flip();

    @classmethod
    def __check_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.__running = False;

    @classmethod
    def __print_letter(self):
        self.__main_surface.fill(self.__background_color);
        self.__main_surface.blit(self.__current_letter.surface, (self.__current_letter.x, self.__current_letter.y));
        self.__current_letter.move();

import random;
from pygame import Surface;
from pygame.font import Font;

class FallingLetter():
    __x: int;
    __y: int = 0;
    __surface: Surface;
    __font: Font;

    @classmethod
    def __init__(self, font, letters, color, surface_size):
        self.__font = font;
        self.__x = random.randint(0, surface_size[1]);
        self.__surface = font.render(random.choice(letters), 1, color);

    @classmethod
    def move(self):
        self.__y += self.__font.get_linesize();

    @property
    def x(self) -> int:
        return self.__x;

    @property
    def y(self) -> int:
        return self.__y;

    @property
    def surface(self) -> Surface:
        return self.__surface;

import random;
from pygame import Surface;
from pygame.font import Font;

class FallingLetter(object):
    @classmethod
    def __init__(self, font, letters, color, min_x, max_x, min_y, max_y):
        self.__font = font;
        self.__surface = font.render(random.choice(letters), 1, color);
        self.__x = random.randint(min_x + self.__font.get_linesize(), max_x - self.__font.get_linesize());
        self.__y = min_y + self.__font.get_linesize();
        self.__max_y = max_y;
        self.__reached_end = False;

    @classmethod
    def move(self):
        y = self.__y + self.__font.get_linesize();
        
        if (not(y >= self.__max_y)):
            self.__y = y;
        else:
            self.__reached_end = True;

    @property
    def x(self) -> int:
        return self.__x;

    @property
    def y(self) -> int:
        return self.__y;

    @property
    def surface(self) -> Surface:
        return self.__surface;

    @property
    def reached_end(self) -> int:
        return self.__reached_end;

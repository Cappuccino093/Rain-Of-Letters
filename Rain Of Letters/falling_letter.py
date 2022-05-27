import json
import pygame;
import random;
import typing;
from pygame import Surface, Rect;
from pygame.font import Font;
from letter import Letter;

if typing.TYPE_CHECKING:
	from rain_of_letters import RainOfLetters;

class FallingLetter(object):
	def __init__(self, rain_of_letters) -> None:
		self.__rain_of_letters: RainOfLetters = rain_of_letters;

		self.__letter: Letter = random.choice(self.__rain_of_letters.letters);

		self.__font: Font = self.__rain_of_letters.font;
		self.__surface: Surface = self.__rain_of_letters.font.render(self.__letter.raw, False, self.__rain_of_letters.primary_color);

		area_rect: Rect = self.__rain_of_letters.area_surface.get_rect();
		font_linesize: int = self.__font.get_linesize();
		self.__x = random.randint(area_rect.x + font_linesize, area_rect.width - font_linesize);
		self.__y = area_rect.y + font_linesize;
		self.__maximum_y = area_rect.height - font_linesize;

		self.__reached_end = False;
		self.__pressed = False;

	@property
	def letter(self) -> Letter:
		return self.__letter;

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
	def reached_end(self) -> bool:
		return self.__reached_end;

	@property
	def pressed(self) -> bool:
		return self.__pressed;
	
	def move(self):
		y = self.__y + self.__font.get_linesize();
		
		if (not(y >= self.__maximum_y)):
			self.__y = y;
		else:
			self.__reached_end = True;

	def press(self):
		if (not self.__reached_end):
			self.__pressed = True;



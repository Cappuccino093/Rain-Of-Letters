import pygame;
import os;
from pygame import Surface;
from pygame.font import Font, SysFont;
from falling_letter import FallingLetter;

class RainOfLetters(object):
	# Surface
	__main_surface: Surface;
	__surface_caption: str = "Rain of Letters"
	__surface_size: tuple[int, int] = (640, 360);

	# Assets
	__background_image_path: str = os.path.join("Assets", "field.png");
	__background_surface: Surface;
	__background_surface_position: tuple[int, int] = (0, 0);

	__area_image_path: str = os.path.join("Assets", "area.png");
	__area_surface: Surface;
	__area_surface_position: tuple[int, int] = (10, 10);

	# Flag
	__running = True;

	# Font
	__font: Font;
	__font_name: str = "Seoge UI Variable";
	__font_size: int = 30;
	
	# Color
	__primary_color: tuple[int, int, int] = (79, 107, 237);

	# Letters
	__predefined_letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	__current_letter: FallingLetter;

	# Clock
	__clock = pygame.time.Clock();
	__framerate = 60;
	__frame: int = 0;

	@classmethod
	def start(self):
		pygame.init();
		pygame.display.set_mode(self.__surface_size, pygame.SCALED | pygame.RESIZABLE | pygame.WINDOWMAXIMIZED);
		pygame.display.set_caption(self.__surface_caption);

		self.__font = SysFont(self.__font_name, self.__font_size);
		self.__main_surface = pygame.display.get_surface();

		self.__background_surface = pygame.image.load(self.__background_image_path);
		self.__area_surface = pygame.image.load(self.__area_image_path);
		
		self.__current_letter = self.__generate_letter();

		while (self.__running):
			self.__clock.tick(self.__framerate);
			self.__frame += 1;

			if ((self.__frame % self.__framerate) == 0):
				self.__frame = 0;
				self.__print();
				self.__check_events();
				pygame.display.flip();

	@classmethod
	def __print(self):
		self.__main_surface.blit(self.__background_surface, self.__background_surface_position);
		self.__main_surface.blit(self.__area_surface, self.__area_surface_position);
		self.__main_surface.blit(self.__current_letter.surface, (self.__current_letter.x, self.__current_letter.y));

		if (not self.__current_letter.reached_end):
			self.__current_letter.move();
		else:
			self.__current_letter = self.__generate_letter();

	@classmethod
	def __generate_letter(self) -> FallingLetter:
		return FallingLetter(self.__font,
						 self.__predefined_letters,
						 self.__primary_color,
						 self.__area_surface.get_rect().x,
						 self.__area_surface.get_rect().width,
						 self.__area_surface.get_rect().y,
						 self.__area_surface.get_rect().height);

	@classmethod
	def __check_events(self):
		for event in pygame.event.get():
			self.__check_quit(event);
			self.__check_key_down(event);

	@classmethod
	def __check_quit(self, event):
		if (event.type == pygame.QUIT):
			self.__running = False;

	@classmethod
	def __check_key_down(self, event):
		if (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_ESCAPE):
				self.__running = False;
			elif (event.key == pygame.K_RETURN):
				pygame.display.toggle_fullscreen();
			
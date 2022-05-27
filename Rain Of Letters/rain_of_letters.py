import pygame;
import typing;
import os;
from pygame import Surface;
from pygame.font import Font, SysFont;
from letter import Letter;
from falling_letter import FallingLetter;
from letters import letters;

class RainOfLetters(object):
	# Fields
	#	Surface
	__main_surface: Surface;
	__surface_caption: str = "Rain of Letters"
	__surface_size: tuple[int, int] = (640, 360);

	#	Assets
	__background_image_path: str = os.path.join("Assets", "field.png");
	__background_surface: Surface;
	__background_surface_position: tuple[int, int] = (0, 0);

	__area_image_path: str = os.path.join("Assets", "area.png");
	__area_surface: Surface;
	__area_surface_position: tuple[int, int] = (10, 10);

	#	Font
	__font: Font;
	__font_name: str = "Seoge UI Variable";
	__font_size: int = 30;
	
	#	Color
	__primary_color: tuple[int, int, int] = (79, 107, 237);

	#	Letters
	__letters: list[Letter] = letters;
	__current_falling_letter: FallingLetter;

	#	Clock
	__clock = pygame.time.Clock();
	__framerate = 60;
	__frame: int = 0;

	# Properties
	@property
	def main_surface(self) -> Surface:
		return self.__main_surface;

	@property
	def surface_caption(self) -> str:
		return self.__surface_caption;

	@property
	def surface_size(self) -> tuple[int, int]:
		return self.__surface_size;

	@property
	def background_image_path(self) -> str:
		return self.__background_image_path;

	@property
	def background_surface(self) -> Surface:
		return self.__background_surface;

	@property
	def background_surface_position(self) -> tuple[int, int]:
		return self.__background_surface_position;

	@property
	def area_image_path(self) -> str:
		return self.__area_image_path;

	@property
	def area_surface(self) -> Surface:
		return self.__area_surface;

	@property
	def area_surface_position(self) -> tuple[int, int]:
		return self.__area_surface_position;

	@property
	def font(self) -> Font:
		return self.__font;

	@property
	def font_name(self) -> str:
		return self.__font_name;

	@property
	def font_size(self) -> int:
		return self.__font_size;

	@property
	def primary_color(self) -> tuple[int, int, int]:
		return self.__primary_color;

	@property
	def letters(self) -> list[Letter]:
		return self.__letters;

	@property
	def framerate(self) -> int:
		return self.__framerate;

	@property
	def frame(self) -> int:
		return self.__frame;

	@property
	def running(self) -> bool:
		return self.__running;

	# Constructor
	def __init__(self) -> None:
		self.__running: bool = True;

	# Methods
	def start(self):
		print(self.__running);
		pygame.init();
		pygame.display.set_mode(self.__surface_size, pygame.SCALED | pygame.RESIZABLE | pygame.WINDOWMAXIMIZED);
		pygame.display.set_caption(self.__surface_caption);

		self.__font = SysFont(self.__font_name, self.__font_size);
		self.__main_surface = pygame.display.get_surface();

		self.__background_surface = pygame.image.load(self.__background_image_path);
		self.__area_surface = pygame.image.load(self.__area_image_path);
		
		self.__current_falling_letter = self.__generate_letter();

		while (self.__running):
			self.__clock.tick(self.__framerate);
			self.__frame += 1;
			self.__check_events();

			if (self.__current_falling_letter.reached_end or self.__current_falling_letter.pressed):
				self.__current_falling_letter = self.__generate_letter();


			if ((self.__frame % self.__framerate) == 0):
				self.__frame = 0;
				self.__print();
				pygame.display.flip();

	def __print(self):
		self.__main_surface.blit(self.__background_surface, self.__background_surface_position);
		self.__main_surface.blit(self.__area_surface, self.__area_surface_position);
		self.__main_surface.blit(self.__current_falling_letter.surface, (self.__current_falling_letter.x, self.__current_falling_letter.y));

		if (not(self.__current_falling_letter.reached_end or self.__current_falling_letter.pressed)):
			self.__current_falling_letter.move();

	def __generate_letter(self) -> FallingLetter:
		return FallingLetter(self);

	def __check_events(self):
		for event in pygame.event.get():
			self.__check_quit(event);
			self.__check_key_down(event);

	def __check_quit(self, event):
		if (event.type == pygame.QUIT):
			self.__running = False;

	def __check_key_down(self, event):
		if (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_ESCAPE):
				self.__running = False;

			elif (event.key == pygame.K_RETURN):
				pygame.display.toggle_fullscreen();
			
			elif (event.key == self.__current_falling_letter.letter.code):
				self.__current_falling_letter.press();
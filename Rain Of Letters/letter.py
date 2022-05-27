import pygame;

class Letter(object):
	def __init__(self, raw, code) -> None:
		self.__raw: str = raw;
		self.__code: int = code;

	@property
	def raw(self) -> str:
		return self.__raw;

	@property
	def code(self) -> int:
		return self.__code;
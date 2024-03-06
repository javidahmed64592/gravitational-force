from __future__ import annotations

import sys
from typing import Any, Dict

import pygame
from helpers.pg import create_font
from pygame.locals import QUIT


class App:
    def __init__(self, fps: int) -> None:
        """
        Initialise application and set FPS.

        Parameters:
            fps (int): Application FPS
        """
        self._fps = fps

    @property
    def screen(self) -> pygame.Surface:
        """
        Get application screen.
        """
        return self._display_surf

    @classmethod
    def create_app(cls, config: Dict[str, Any]):
        """
        Create application using app config.

        Parameters:
            config (Dict[str, Any]): App config

        Returns:
            _app (App): App with screen, clock, and font set.
        """
        pygame.init()
        _app = cls(fps=config["fps"])
        _app._add_clock()
        _app._set_font(font=config["font"]["font"], font_size=config["font"]["size"])
        _app._create_screen(width=config["screen"]["width"], height=config["screen"]["height"])
        _app._set_screen_name(name=config["screen"]["name"])
        return _app

    def _add_clock(self) -> None:
        """
        Add a Pygame clock.
        """
        self._clock = pygame.time.Clock()

    def _create_screen(self, width: int, height: int) -> None:
        """
        Create and configure application screen dimensions.

        Parameters:
            width (int): Screen width
            height (int): Screen height
        """
        self._width = width
        self._height = height
        self._display_surf = pygame.display.set_mode((self._width, self._height))

    def _set_screen_name(self, name: str) -> None:
        """
        Set screen name.

        Parameters:
            name (str): Screen name
        """
        self._name = name
        pygame.display.set_caption(self._name)

    def _set_font(self, font: str, font_size: int) -> None:
        """
        Set application font.

        Parameters:
            font (str): Font style to use
            font_size (int): Font size for text
        """
        self._font = font
        self._font_size = font_size
        self._pg_font = create_font(self._font, self._font_size)

    def write_text(self, text: str, x: float, y: float) -> None:
        """
        Write text to the screen at the given position.

        Parameters:
            text (str): Text to write
            x (float): x coordinate of text's position
            y (float): y coordinate of text's position
        """
        text_to_write = self._pg_font.render(text, False, (255, 255, 255))
        self._display_surf.blit(text_to_write, (x, y))

    def update(self) -> None:
        """
        Display application information to screen.
        """
        start_x = 50
        start_y = 50
        self.write_text("App info:", start_x, start_y)
        self.write_text(f"Name: {self._name}", start_x, start_y * 3)
        self.write_text(f"Width: {self._width}", start_x, start_y * 4)
        self.write_text(f"Height: {self._height}", start_x, start_y * 5)
        self.write_text(f"Font: {self._font}", start_x, start_y * 6)
        self.write_text(f"Font size: {self._font_size}", start_x, start_y * 7)
        self.write_text(f"FPS: {self._clock.get_fps()}", start_x, start_y * 9)

    def run(self) -> None:
        """
        Run the application and handle events.
        """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self._display_surf.fill((0, 0, 0))

            self.update()
            pygame.display.update()
            self._clock.tick(self._fps)

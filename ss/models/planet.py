from __future__ import annotations

from typing import Any, Dict, List

import pygame
from helpers.pg import create_font
from models.body import Body
from numpy.typing import NDArray
from pg.shapes import PygameCircle


class Planet(Body):
    def __init__(self, name: str, mass: float, start_pos: NDArray, start_vel: NDArray, start_acc: NDArray) -> None:
        """
        Initialise Planet object with name and physical components.

        Parameters:
            name (str): Name of planet
            mass (float): Mass of planet
            start_pos (NDArray): Starting position of planet
            start_vel (NDArray): Starting velocity of planet
            start_acc (NDArray): Starting acceleration of planet
        """
        super().__init__(name, mass, start_pos, start_vel, start_acc)

    @classmethod
    def create_planet(cls, config: Dict[str, Any], text_config: Dict[str, Any]) -> Planet:
        """
        Create planet using planet config and font style/size.

        Parameters:
            config (Dict[str, Any]): Planet config
            text_config (Dict[str, Any]): Font config

        Returns:
            _planet (Planet): Planet with shape and text to draw to Pygame screen
        """
        _planet: Planet = cls.from_config(config)
        _planet._set_font(text_config["font"], text_config["size"])
        _planet._set_shape(config["colour"])
        return _planet

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw planet to screen.

        Parameters:
            screen (Surface): Pygame screen
        """
        self._shape.draw(screen)
        text_to_write = self._pg_font.render(self._name, False, (255, 255, 255))
        screen.blit(text_to_write, (self._pos[0], self._pos[1] - 10))

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

    def _set_shape(self, colour: List[float]) -> None:
        """
        Set shape colour and dimensions to draw to screen.

        Parameters:
            colour (List[float]): RGB values
        """
        self._colour = colour
        self._shape = PygameCircle(self._colour, self._pos, self._mass)

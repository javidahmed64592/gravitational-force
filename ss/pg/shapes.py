from typing import Tuple, cast

import pygame


class Shape:
    def __init__(self, colour: Tuple[int, int, int], pos: Tuple[float], size: float | Tuple[float]) -> None:
        """
        Initialise shape with colour, position and size.

        Parameters:
            colour (Tuple[int, int, int]): Colour value of shape
            pos (Tuple[float]): Position of shape
            size (float | List[float]): Size of shape
        """
        self._colour = colour
        self._pos = pos
        self._size = size

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw shape to Pygame screen.

        Parameters:
            screen (Surface): Pygame screen to draw shape
        """
        pass


class PygameCircle(Shape):
    def __init__(self, colour: Tuple[int, int, int], pos: Tuple[float], size: float) -> None:
        """
        Initialise a Pygame circle.

        Parameters:
            colour (Tuple[int, int, int]): Colour value of circle
            pos (Tuple[float]): Position of circle
            size (float): Radius of circle
        """
        super().__init__(colour, pos, size)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw circle to Pygame screen.

        Parameters:
            screen (Surface): Pygame screen to draw circle
        """
        pygame.draw.circle(screen, self._colour, self._pos, cast(float, self._size))


class PygameRect(Shape):
    def __init__(self, colour: Tuple[int, int, int], pos: Tuple[float], size: Tuple[float]) -> None:
        """
        Initialise a Pygame rectangle.

        Parameters:
            colour (Tuple[int, int, int]): Colour value of rectangle
            pos (Tuple[float]): Position of rectangle
            size (Tuple[float]): [Width, Height] of rectangle
        """
        super().__init__(colour, pos, size)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw rectangle to Pygame screen.

        Parameters:
            screen (Surface): Pygame screen to draw rectangle
        """
        pygame.draw.rect(screen, self._colour, self._pos + self._size)

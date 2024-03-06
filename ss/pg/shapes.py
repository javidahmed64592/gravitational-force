from typing import List

import pygame


class Shape:
    def __init__(self, colour: List[float], pos: List[float], size: float | List[float]) -> None:
        """
        Initialise shape with colour, position and size.

        Parameters:
            colour (List[float]): Colour value of shape
            pos (List[float]): Position of shape
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
    def __init__(self, colour: List[float], pos: List[float], size: float) -> None:
        """
        Initialise a Pygame circle.

        Parameters:
            colour (List[float]): Colour value of circle
            pos (List[float]): Position of circle
            size (float): Radius of circle
        """
        super().__init__(colour, pos, size)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw circle to Pygame screen.

        Parameters:
            screen (Surface): Pygame screen to draw circle
        """
        pygame.draw.circle(screen, self._colour, self._pos, self._size)


class PygameRect(Shape):
    def __init__(self, colour: List[float], pos: List[float], size: List[float]) -> None:
        """
        Initialise a Pygame rectangle.

        Parameters:
            colour (List[float]): Colour value of rectangle
            pos (List[float]): Position of rectangle
            size (List[float]): [Width, Height] of rectangle
        """
        super().__init__(colour, pos, size)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw rectangle to Pygame screen.

        Parameters:
            screen (Surface): Pygame screen to draw rectangle
        """
        pygame.draw.rect(screen, self._colour, self._pos + self._size)

import pygame


def create_font(font: str, size: int) -> pygame.font.Font:
    """
    Create a Pygame font.

    Parameters:
        font (str): Font style
        size (int): Font size

    Returns:
        (Font): Pygame font
    """
    return pygame.font.SysFont(font, size)

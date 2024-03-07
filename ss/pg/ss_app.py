from typing import Any, Dict

import numpy as np
from models.planet import Planet
from pg.app import App


class SolarSystemApp(App):
    def __init__(self, fps: int) -> None:
        """
        Initialise the Solar System application.

        Parameters:
            fps (int): Application FPS
        """
        super().__init__(fps)

    def add_planets(self, config: Dict[str, Any]) -> None:
        """
        Add planets from config.

        Parameters:
            config (Dict[str, Any]): Planet config
        """
        self._planets = [Planet.create_planet(planet_config, config["font"]) for planet_config in config["planets"]]
        Planet.G = config["G"]
        Planet.dt = config["dt"]

    def update(self):
        """
        Calculate gravitational forces between planets and move accordingly.
        """
        self.move_planets()
        self.draw_planets()

    def move_planets(self):
        """
        Calculate gravitational force between each planet and move accordingly.
        """
        for planet in self._planets:
            force = np.sum([planet.calculate_force(other_planet) for other_planet in self._planets], axis=0)
            planet.apply_force(force)
            planet.move()

    def draw_planets(self):
        """
        Draw each planet to the screen.
        """
        for planet in self._planets:
            planet.draw(self._display_surf)

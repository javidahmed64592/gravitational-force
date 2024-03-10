from __future__ import annotations

from typing import Any, Dict

import numpy as np
from numpy.typing import NDArray
from pg.shapes import Shape


class Body:
    G = 5
    dt = 1

    def __init__(
        self,
        name: str,
        mass: float,
        density: float,
        start_pos: NDArray,
        start_vel: NDArray,
        start_acc: NDArray,
    ):
        """
        Initialise a Body object with name and physical attributes.

        Parameters:
            name (str): Name of body
            mass (float): Mass of body
            density (float): Density of body
            start_pos (NDArray): Starting position of body
            start_vel (NDArray): Starting velocity of body
            start_acc (NDArray): Starting acceleration of body
        """
        self._name = name
        self._mass = mass
        self._density = density
        self._r = np.cbrt(self._mass / self._density)
        self._pos = start_pos
        self._vel = start_vel
        self._acc = start_acc
        self._shape: Shape

    @property
    def mass(self):
        """
        Return body mass.
        """
        return self._mass

    @property
    def pos(self):
        """
        Return body position.
        """
        return self._pos

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> Body:
        """
        Create Body using config.

        Parameters:
            config (Dict[str, Any]): Body config with name, mass, position, velocity, acceleration

        Returns:
            _body (Body): Body with set name and physical attributes
        """
        _name = config["name"]
        _mass = config["mass"]
        _density = config["density"]
        _pos = np.array(config["pos"], dtype=np.float64)
        _vel = np.array(config["vel"], dtype=np.float64)
        _acc = np.array(config["acc"], dtype=np.float64)
        _body = cls(_name, _mass, _density, _pos, _vel, _acc)
        return _body

    @staticmethod
    def normalise_vector(v: NDArray) -> NDArray:
        """
        Normalise a vector.

        Parameters:
            v (NDArray): Vector to normalise

        Returns:
            (NDArray): Normalised vector
        """
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        normalised_v: NDArray = v / norm
        return normalised_v

    @staticmethod
    def calculate_r(pos: NDArray, other_pos: NDArray) -> float:
        """
        Calculate distance between two positions.

        Parameters:
            pos (NDArray): Position A
            other_pos (NDArray): Position B

        Returns:
            _r (float): Distance between position A and B
        """
        _pos_dif = other_pos - pos
        _r: float = np.sqrt(np.sum(np.square(_pos_dif)))
        return _r

    def calculate_force(self, other_body: Body) -> NDArray:
        """
        Calculate gravitational force on self due to other body.

        Parameters:
            other_body (Body): Body exerting force on self

        Returns:
            force_arr (NDArray): Gravitational force array
        """
        if other_body is self:
            return np.array([0, 0])

        pos_dif = other_body.pos - self._pos
        r = Body.calculate_r(self._pos, other_body.pos)
        r = np.max([r, 1])
        if r <= self._r:
            return np.zeros((2,))
        f = (self.G * self._mass * other_body.mass) / (r**2)
        force_arr: NDArray = Body.normalise_vector(pos_dif) * f
        return force_arr

    def apply_force(self, force: NDArray) -> None:
        """
        Set acceleration from net force on self.

        Parameters:
            force (NDArray): Net force on body
        """
        self._acc = force / self._mass

    def move(self):
        """
        Move body after acceleration.
        """
        self._vel += self._acc * self.dt
        self._pos += self._vel * self.dt

from __future__ import annotations

from typing import Any, Dict, List

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


class SolarGraph:
    def __init__(self):
        self._fig: Figure
        self._ax: Axes
        self._title: str
        self._x_label: str
        self._y_label: str
        self._x_lims: List[float]
        self._y_lims: List[float]

    @property
    def ax(self) -> Axes:
        return self._ax

    @classmethod
    def create_graph(cls, config: Dict[str, Any]) -> SolarGraph:
        _title = config["title"]
        _x_label = config["x_label"]
        _y_label = config["y_label"]
        _x_lims = config["x_lims"]
        _y_lims = config["y_lims"]
        _figsize = config["figsize"]
        _solar_graph: SolarGraph = cls()
        _solar_graph._generate_ax(_figsize)
        _solar_graph._configure_ax(_title, _x_label, _y_label)
        _solar_graph._update_ax_lims(_x_lims, _y_lims)
        return _solar_graph

    @staticmethod
    def show():
        plt.show()

    def _generate_ax(self, figsize: List[float]) -> None:
        self._fig, self._ax = plt.subplots(1, 1, figsize=figsize)

    def _configure_ax(self, title: str, x_label: str, y_label: str) -> None:
        self._title = title
        self._x_label = x_label
        self._y_label = y_label

        self._ax.set_title(self._title)
        self._ax.set_xlabel(self._x_label)
        self._ax.set_ylabel(self._y_label)

    def _update_ax_lims(self, x_lims: List[float], y_lims: List[float]) -> None:
        self._x_lims = x_lims
        self._y_lims = y_lims

        self._ax.set_xlim(self._x_lims)
        self._ax.set_ylim(self._y_lims)

    def legend(self) -> None:
        self._ax.legend()

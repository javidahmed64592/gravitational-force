import os
from pathlib import Path

from helpers.config import load_config
from pg.ss_app import SolarSystemApp

CWD = Path(os.path.abspath(__file__)).parent
CONFIG_FOLDER = CWD / "config"

if __name__ == "__main__":
    app_config = load_config(CONFIG_FOLDER / "app.json")
    app = SolarSystemApp.create_app(app_config)
    planet_config = load_config(CONFIG_FOLDER / "planets.json")
    app.add_planets(planet_config)
    app.run()

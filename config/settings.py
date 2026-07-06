from pathlib import Path

import yaml


class Settings:
    """Loads and provides access to application configuration."""

    _config = None

    @classmethod
    def load(cls):
        """Load configuration from YAML file."""
        if cls._config is None:
            config_path = Path(__file__).parent / "config.yaml"

            with open(config_path, encoding="utf-8") as file:
                cls._config = yaml.safe_load(file)

    @classmethod
    def get(cls, key):
        """Return configuration value."""
        cls.load()

        environment = cls._config["environment"]

        if key == "base_url":
            return cls._config[environment]["base_url"]

        if key not in cls._config:
            raise KeyError(f"Configuration key '{key}' not found.")

        return cls._config.get(key)

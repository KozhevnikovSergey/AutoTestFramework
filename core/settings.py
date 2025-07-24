import yaml
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Optional

CONFIG_FILE_NAME = "config.yaml"


class Platform(StrEnum):
    WEB = "WEB"
    MOBILE = "MOBILE"


@dataclass
class DeviceConfig:
    type: str


@dataclass
class BrowserConfig:
    headless: bool
    device: DeviceConfig


@dataclass
class TestConfig:
    base_url: str


@dataclass
class EnvironmentConfig:
    platform: Platform


@dataclass
class Config:
    browser: BrowserConfig
    test: TestConfig
    environment: EnvironmentConfig

    @classmethod
    def _get_path(cls, config_path: Optional[str]) -> str:
        if config_path is not None:
            return config_path

        config_file = Path.cwd() / CONFIG_FILE_NAME
        if config_file.exists():
            return str(config_file)

        raise FileNotFoundError(
            f"Config file '{CONFIG_FILE_NAME}' not found in current directory"
        )

    @classmethod
    def load_from_yaml(cls, config_path: Optional[str] = None) -> "Config":
        with open(cls._get_path(config_path), "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return cls(
            browser=BrowserConfig(
                headless=data["browser"]["headless"],
                device=DeviceConfig(type=data["browser"]["device"]["type"]),
            ),
            test=TestConfig(
                base_url=data["test"]["base_url"],
            ),
            environment=EnvironmentConfig(
                platform=Platform(data["environment"]["platform"]),
            ),
        )

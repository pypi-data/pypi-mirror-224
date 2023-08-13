from geneweaver.db.core.settings_class import Settings as DBSettings
from pydantic import BaseSettings


class SettingsTest(BaseSettings):
    DEBUG_MODE = False
    DB_SETTINGS: DBSettings = DBSettings()

    class Config:
        """Configuration for the BaseSettings class."""

        env_file = ".env"
        case_sensitive = True

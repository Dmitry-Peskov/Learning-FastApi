from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    version: str
    debug: bool

    model_config = SettingsConfigDict(env_prefix="app_", env_file=".env")


app_settings = AppSettings()

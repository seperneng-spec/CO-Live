from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CO-Live"
    app_env: str = "development"
    secret_key: str = "change-me"
    database_url: str = "postgresql://postgres:postgres@db:5432/co_live"
    webhook_secret: str = "change-me"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

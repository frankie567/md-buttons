from pydantic import BaseSettings


class Settings(BaseSettings):
    font: str = "LiberationSans-Regular.ttf"
    http_cache_ttl: int = 24 * 60 * 3600

    class Config:
        env_file = ".env"


settings = Settings()

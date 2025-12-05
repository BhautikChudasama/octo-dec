from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "NodeOps Pricing API"


settings = Settings()

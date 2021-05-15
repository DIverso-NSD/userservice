from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    psql_url: str = Field(..., env="PSQL_URL")
    secret_key: str = Field(..., env="SECRET_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings(_env_file="../.env")

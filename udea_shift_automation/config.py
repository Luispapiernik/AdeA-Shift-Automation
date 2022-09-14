from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    username: str = Field(None, env="USER_NAME")
    password: str = Field(None, env="PASSWORD")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

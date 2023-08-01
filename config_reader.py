from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = '.env'
        env_encode = 'utf-8'


config = Setting()

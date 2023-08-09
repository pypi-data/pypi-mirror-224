from pydantic import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = 'local'

    AWS_REGION: str = 'ap-southeast-1'


settings = Settings()

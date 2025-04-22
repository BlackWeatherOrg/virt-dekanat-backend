import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str
    PORT: int

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 14400  # 10 days

    APP_DIR: str = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__) or '.'))

    model_config = SettingsConfigDict(
        env_file=f'{APP_DIR}/settings/settings.env')

    def create_db_url(self):
        return 'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(self.POSTGRES_USER, self.POSTGRES_PASSWORD,
                                                            self.POSTGRES_HOST, self.POSTGRES_PORT,
                                                            self.POSTGRES_DB)


settings = Settings()

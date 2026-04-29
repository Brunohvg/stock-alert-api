from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Stock Alert API'
    ENVIRONMENT: str = 'development'
    DATABASE_URL: str
    LOG_LEVEL: str = 'INFO'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='ignore',
    )


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Stock Alert API"
    
    # Se você deixar sem valor padrão, o Pydantic obriga 
    # que ela exista no .env (excelente para evitar erros em produção)
    DATABASE_URL: str 

    # Permite ler o arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        case_sensitive=True
    )

settings = Settings()
"""
Configurações globais da aplicação.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Carrega as configurações da aplicação."""

    # Informações da aplicação
    APP_NAME: str = "ATLAS AI"
    APP_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"

    # Ambiente
    DEBUG: bool = True

    # Banco de dados
    DATABASE_URL: str = (
        "postgresql://atlas:atlas@localhost:5432/atlas"
    )

    # IA
    OPENAI_API_KEY: str = ""

    # Arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


# Instância global das configurações
settings = Settings()

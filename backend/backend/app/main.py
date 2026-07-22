"""
ATLAS AI

Ponto de entrada da aplicação FastAPI.
"""

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging


# Inicializa o sistema de logs
setup_logging()


# Cria a aplicação
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Software Engineering Platform",
)


@app.get("/")
async def root():
    """Verifica se a API está online."""

    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }

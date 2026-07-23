"""
Configuração do sistema de logs.
"""

import logging


def setup_logging() -> None:
    """Inicializa os logs da aplicação."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

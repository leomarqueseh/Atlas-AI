"""
====================================================
ATLAS AI
Backend Agent

Responsável por gerar toda a arquitetura Backend
utilizando Python e FastAPI.
====================================================
"""


class BackendAgent:

    def __init__(self):
        """
        Construtor da classe.

        Armazena informações básicas do agente.
        """
        self.name = "Backend Architect"

    def generate(self, prompt: str):
        """
        Gera uma resposta simulando a criação
        de um projeto Backend.

        Parameters
        ----------
        prompt : str
            Descrição enviada pelo usuário.

        Returns
        -------
        dict
            Informações do agente responsável.
        """

        return {
            "agent": self.name,
            "language": "Python",
            "framework": "FastAPI",
            "response": f"Generating backend for: {prompt}"
        }
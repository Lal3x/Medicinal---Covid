# src/medicinal/config/settings.py
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def get_env_var(
    nome: str, obrigatoria: bool = True, default: str | None = None
) -> str | None:
    """
    Busca uma variável de ambiente, com opção de ser obrigatória ou não.
    Levanta erro claro se for obrigatória e não estiver definida.
    """
    valor = os.getenv(nome, default)

    if obrigatoria and not valor:
        raise ValueError(f"Variável de ambiente obrigatória não encontrada: {nome}")

    return valor


# Banco de dados
DATABASE_URL: str = get_env_var("DATABASE_URL")

# Ambiente da aplicação (dev, staging, prod)
APP_ENV: str = get_env_var("APP_ENV", obrigatoria=False, default="dev")

# Nível de log
LOG_LEVEL: str = get_env_var("LOG_LEVEL", obrigatoria=False, default="INFO")

# Nomes dos schemas no Postgres
SCHEMA_BRONZE: str = get_env_var("SCHEMA_BRONZE", obrigatoria=False, default="bronze")
SCHEMA_SILVER: str = get_env_var("SCHEMA_SILVER", obrigatoria=False, default="silver")
SCHEMA_GOLD: str = get_env_var("SCHEMA_GOLD", obrigatoria=False, default="gold")

# Diretório de dados (landing zone dos CSVs brutos)
RAW_DATA_DIR: Path = Path(
    get_env_var("RAW_DATA_DIR", obrigatoria=False, default="data/raw")
)

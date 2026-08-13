# src/medicinal/bronze/ingest.py
from sqlalchemy.engine import Engine

from medicinal.bronze.readers import (
    add_execution_metadata,
    read_csv_lowercase,
    validate_not_empty,
)
from medicinal.config.settings import RAW_DATA_DIR, SCHEMA_BRONZE
from medicinal.utils.db import get_engine
from medicinal.utils.schema import create_schemas

# Mapeia nomes das tabelas de destino para os nomes dos arquivos CSV de origem.
FILES = {
    "bronze_patients": "patients.csv",
    "bronze_encounters": "encounters.csv",
    "bronze_conditions": "conditions.csv",
}


def load_bronze(engine: Engine | None = None) -> None:
    """
    Lê os CSVs da landing zone (raw) e carrega no schema bronze do Postgres.
    Cada tabela é recriada do zero a cada execução ('replace').
    """
    engine = engine or get_engine()

    for table_name, filename in FILES.items():
        path = RAW_DATA_DIR / filename
        print(f"Lendo {path}...")

        df = read_csv_lowercase(path)

        if not validate_not_empty(df, filename):
            continue

        df = add_execution_metadata(df)

        df.to_sql(
            name=table_name,
            con=engine,
            schema=SCHEMA_BRONZE,
            if_exists="replace",
            index=False,
        )

        print(f"{len(df)} linhas carregadas em {SCHEMA_BRONZE}.{table_name}")

    print("\nCarga bronze concluída.")


if __name__ == "__main__":
    create_schemas()
    load_bronze()

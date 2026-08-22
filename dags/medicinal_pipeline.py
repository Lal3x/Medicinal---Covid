from datetime import UTC, datetime
from pathlib import Path

from airflow.sdk import dag, task


@dag(
    dag_id="medicinal_pipeline",
    description="Executa o pipeline de dados bronze, silver e gold.",
    start_date=datetime(2026, 8, 22, tzinfo=UTC),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["medicinal", "etl"],
)
def medicinal_pipeline():
    @task
    def verificar_banco() -> None:
        from medicinal.utils.db import get_engine

        engine = get_engine()
        engine.dispose()

    @task
    def verificar_arquivos() -> None:
        from medicinal.bronze.ingest import FILES
        from medicinal.config.settings import RAW_DATA_DIR

        ausentes = [
            filename
            for filename in FILES.values()
            if not (Path(RAW_DATA_DIR) / filename).is_file()
        ]

        if ausentes:
            raise FileNotFoundError(f"Arquivos CSV ausentes: {', '.join(ausentes)}")

    @task
    def criar_schemas() -> None:
        from medicinal.utils.schema import create_schemas

        create_schemas()

    @task
    def carregar_bronze() -> None:
        from medicinal.bronze.ingest import load_bronze

        load_bronze()

    @task
    def transformar_silver() -> None:
        from medicinal.silver.transform import load_silver

        load_silver()

    @task
    def agregar_gold() -> None:
        from medicinal.gold.aggregate import load_gold

        load_gold()

    banco = verificar_banco()
    arquivos = verificar_arquivos()
    schemas = criar_schemas()
    bronze = carregar_bronze()
    silver = transformar_silver()
    gold = agregar_gold()

    [banco, arquivos] >> schemas >> bronze >> silver >> gold


medicinal_pipeline()

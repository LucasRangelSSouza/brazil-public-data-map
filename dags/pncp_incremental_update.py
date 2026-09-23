"""Portable Airflow template. Connection IDs and output paths come from the deployer's environment."""

from pathlib import Path

from brazil_data_map.pipeline import build_public_release

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:  # The repository must remain importable without Airflow.
    DAG = None
    PythonOperator = None


def run_incremental_release(records: list[dict], output_root: str) -> None:
    """Write a reviewed local release candidate after the deployer supplies source records."""
    build_public_release(
        records=records,
        output_root=Path(output_root),
        source_id="pncp",
        source_url="https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos",
    )


if DAG is not None:
    with DAG("pncp_incremental_update", schedule="0 */6 * * *", catchup=False) as dag:
        PythonOperator(task_id="incremental_release", python_callable=run_incremental_release)

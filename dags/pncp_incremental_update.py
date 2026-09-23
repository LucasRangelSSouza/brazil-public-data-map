"""Portable Airflow template. Connection IDs and output paths come from the deployer's environment."""

from datetime import date
from pathlib import Path

from brazil_data_map.pipeline import build_public_release
from brazil_data_map.pncp import fetch_publications

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:  # The repository must remain importable without Airflow.
    DAG = None
    PythonOperator = None


def run_incremental_release(start: str, end: str, modality_id: int, output_root: str) -> None:
    """Fetch a bounded PNCP publication window and write a local release candidate."""
    records = fetch_publications(date.fromisoformat(start), date.fromisoformat(end), modality_id)
    build_public_release(
        records=records,
        output_root=Path(output_root),
        source_id="pncp",
        source_url="https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao",
    )


if DAG is not None:
    with DAG("pncp_incremental_update", schedule="0 */6 * * *", catchup=False) as dag:
        PythonOperator(task_id="incremental_release", python_callable=run_incremental_release)

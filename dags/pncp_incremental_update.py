"""Portable Airflow template. Connection IDs and output paths come from the deployer's environment."""

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:  # The repository must remain importable without Airflow.
    DAG = None
    PythonOperator = None


def run_incremental_release() -> None:
    """Deployment owners wire this task to their approved local storage and PNCP client."""
    raise RuntimeError("Configure an approved PNCP client and local output path before scheduling this template")


if DAG is not None:
    with DAG("pncp_incremental_update", schedule="0 */6 * * *", catchup=False) as dag:
        PythonOperator(task_id="incremental_release", python_callable=run_incremental_release)


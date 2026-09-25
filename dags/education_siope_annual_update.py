"""Portable Airflow template for the annual SIOPE education release candidate.

The deployer supplies the output directory through the Airflow param
`output_root`; the template carries no connection or credential. Publication stays a separate, reviewed operation.
"""

from datetime import datetime, timezone
from pathlib import Path

from brazil_data_map.pipeline import build_public_release
from brazil_data_map.siope import SIOPE_ODATA_URL, build_records, capture

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:  # The repository must remain importable without Airflow.
    DAG = None
    PythonOperator = None


def run_annual_release(start_year: int, end_year: int, output_root: str) -> dict:
    """Capture SIOPE declarations for the years and build a local, unpublished candidate."""
    root = Path(output_root)
    capture(range(int(start_year), int(end_year) + 1), root / "capture")
    result = build_public_release(
        build_records(root / "capture"),
        root / "candidate",
        "fnde-siope",
        SIOPE_ODATA_URL,
        retrieved_at=datetime.now(timezone.utc).isoformat(),
    )
    return {"record_counts": result["audit"]["record_counts"], "privacy_gate": result["audit"]["privacy_gate"]}


if DAG is not None:
    with DAG(
        "education_siope_annual_update",
        schedule=None,
        start_date=datetime(2026, 1, 1),
        catchup=False,
        is_paused_upon_creation=True,
        params={"start_year": 2019, "end_year": 2023, "output_root": "/tmp/brazil-education-release"},
        tags=["public-data", "template"],
    ) as dag:
        PythonOperator(
            task_id="annual_release_candidate",
            python_callable=run_annual_release,
            op_kwargs={
                "start_year": "{{ params.start_year }}",
                "end_year": "{{ params.end_year }}",
                "output_root": "{{ params.output_root }}",
            },
        )

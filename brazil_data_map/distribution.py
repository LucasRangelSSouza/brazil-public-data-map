from __future__ import annotations

from typing import Any


def validate_distribution_profile(profile: dict[str, Any]) -> None:
    required = {"schema_version", "distribution_status", "datasets"}
    missing = sorted(required - profile.keys())
    if missing:
        raise ValueError(f"distribution profile missing required fields: {', '.join(missing)}")
    if profile["distribution_status"] not in {"pending", "ready", "mixed"}:
        raise ValueError("distribution_status must be pending, ready, or mixed")
    if not isinstance(profile["datasets"], list) or not profile["datasets"]:
        raise ValueError("distribution profile requires at least one dataset")
    for dataset in profile["datasets"]:
        if not dataset.get("intended_slug"):
            raise ValueError("dataset requires an intended_slug")
        dataset_status = dataset.get("distribution_status", profile["distribution_status"])
        if dataset_status not in {"pending", "ready"}:
            raise ValueError("dataset distribution_status must be pending or ready")
        if dataset_status == "ready":
            missing_ready = [field for field in ("published_slug", "version", "review_approval") if not dataset.get(field)]
            if missing_ready:
                raise ValueError(f"ready dataset missing required release evidence: {', '.join(missing_ready)}")

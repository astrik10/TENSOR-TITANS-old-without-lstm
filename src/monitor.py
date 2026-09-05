"""
monitor.py
YOUR JOB:
Logging and live-monitoring helpers: per-tick prediction logging, rolling
accuracy, latency tracking, and a simple drift flag.
"""

from typing import Dict, List, Optional
import json
import os
import time

LOG_PATH = os.path.join("logs", "predictions.jsonl")
RUN_LOG_PATH = "run_log.json"


def log_prediction(
    timestamp: str,
    features: Dict[str, float],
    predictions: Dict[str, int],
    actual: Optional[int],
    latency_ms: float,
) -> None:
    """
    Append one line of JSON to logs/predictions.jsonl recording:
        timestamp, features, predictions (per model), actual (may be None
        until the next tick arrives), latency_ms.

    Create the logs/ directory if it doesn't exist.
    """
    return


def compute_rolling_accuracy(model_name: str, window: int = 50) -> float:
    """
    Read logs/predictions.jsonl and compute accuracy for `model_name` over
    the last `window` ticks that have a non-null `actual` value.

    Returns:
        accuracy as a float in [0, 1]. Return 0.0 if there's no data yet.
    """
    return 0.0


def compute_drift_flag(
    current_volatility: float, training_volatility: float, threshold: float = 1.5
) -> bool:
    """
    Return True if current_volatility is more than `threshold`x the
    volatility seen during training (a simple, cheap drift signal).
    """
    return True


def write_run_log(metadata: Dict) -> None:
    """
    Write/overwrite run_log.json with run metadata, e.g.:
        {
          "start_time": "...",
          "model_versions": {"logreg": "models/logreg_v1_....pkl", ...},
          "total_ticks_processed": 123,
          "final_accuracy": {"logreg": 0.55, "random_forest": 0.58}
        }
    """
    return

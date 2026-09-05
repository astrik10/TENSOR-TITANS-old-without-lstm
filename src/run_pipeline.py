"""
run_pipeline.py
YOUR JOB:
orchestration only; the pieces live in features.py, models.py, monitor.py.

This is the main entry point. It should:
    1. Bootstrap: load data/historical_ticks.csv (or wait for live ticks)
       and build an initial training set using features.compute_features()
       and features.make_label().
    2. Train: call models.train_models() on the bootstrap set.
    3. Serve: poll data/live_ticks.csv (written by scraper.py) for new ticks,
       maintain a rolling buffer, compute features for each new tick,
       get predictions from both models, and log them.
    4. Once the next tick arrives, back-fill the actual outcome for the
       previous prediction and log it via monitor.log_prediction().
    5. Periodically print/update a simple monitoring view (accuracy, tick
       count, latency, drift flag) CLI print loop or Streamlit, your choice.
    6. On shutdown (or every N ticks), call models.save_models() and
       monitor.write_run_log().

Run with:
    python src/run_pipeline.py

Make sure scraper.py is running in a separate terminal if you want to test
against live data. For development, you can point this at
data/historical_ticks.csv first so you're not blocked waiting on live ticks.
"""

import csv
import os
import time

from src.features import compute_features, make_label  # TODO: implement these
from src.models import train_models, predict, save_models  # TODO: implement these
from src.monitor import (  # TODO: implement these
    log_prediction,
    compute_rolling_accuracy,
    compute_drift_flag,
    write_run_log,
)

BUFFER_SIZE = 20
BOOTSTRAP_SOURCE = os.path.join("data", "historical_ticks.csv")
LIVE_SOURCE = os.path.join("data", "live_ticks.csv")


def load_ticks_csv(path):
    """Load a tick CSV into a list of dicts. Provided helper feel free to reuse."""
    ticks = []
    if not os.path.exists(path):
        return ticks
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ticks.append(
                {
                    "timestamp": row["timestamp"],
                    "coin": row["coin"],
                    "price_usd": float(row["price_usd"]),
                }
            )
    return [t for t in ticks if t["coin"] == "bitcoin"]


def bootstrap():
    """
    TODO:
        Load BOOTSTRAP_SOURCE.
        Slide a window of size BUFFER_SIZE across it, computing features
        and labels for each valid position.
        Return (X, y, training_volatility) so run_pipeline() can train
        the models and set a baseline for the drift flag.
    """
    return ()


def run_pipeline():
    """
    TODO: wire everything together per the module docstring above.
    This is intentionally left as an exercise the goal is for you to
    design the ingestion loop, not just fill in blanks.
    """
    return


if __name__ == "__main__":
    run_pipeline()

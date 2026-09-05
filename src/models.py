"""
models.py

Trains and serves the two required classical ML models — Logistic
Regression and Random Forest — on the feature vectors produced by
features.py, and persists them to disk with versioned filenames so
run_pipeline.py / monitor.py can track which artifact produced which
predictions.
"""

from typing import Dict, List
import glob
import os
import pickle
import re
import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

MODELS_DIR = "models"


def train_models(X: List[List[float]], y: List[int]) -> Dict[str, object]:
    """
    Train Logistic Regression and Random Forest on the bootstrap dataset.

    Args:
        X: list of feature vectors (each a list of floats, in a fixed
           feature order you define — e.g. [rolling_mean_5, rolling_mean_20,
           momentum_5, rolling_vol_10]).
        y: list of labels (0/1), same length as X.

    Returns:
        dict like {"logreg": <fitted model>, "random_forest": <fitted model>}

    Raises:
        ValueError: if X/y are empty, mismatched in length, or y doesn't
            contain both classes (a classifier can't learn from one class).
    """
    if not X or not y:
        raise ValueError("train_models requires a non-empty X and y")
    if len(X) != len(y):
        raise ValueError(f"X and y length mismatch: {len(X)} vs {len(y)}")
    if len(set(y)) < 2:
        raise ValueError(
            "Need at least two label classes (0 and 1) to train a classifier; "
            f"got only {set(y)}. Collect more bootstrap data."
        )

    logreg = LogisticRegression(max_iter=1000, random_state=42)
    logreg.fit(X, y)

    random_forest = RandomForestClassifier(n_estimators=200, random_state=42)
    random_forest.fit(X, y)

    return {"logreg": logreg, "random_forest": random_forest}


def predict(models: Dict[str, object], feature_vector: List[float]) -> Dict[str, int]:
    """
    Get a prediction (0 or 1) from each trained model for one feature vector.

    Args:
        models: dict returned by train_models().
        feature_vector: single feature vector, same order used in training.

    Returns:
        dict like {"logreg": 1, "random_forest": 0}

    Raises:
        ValueError: if models is empty.
    """
    if not models:
        raise ValueError("predict requires a non-empty models dict")

    vector_2d = [list(feature_vector)]
    predictions: Dict[str, int] = {}
    for name, model in models.items():
        predictions[name] = int(model.predict(vector_2d)[0])
    return predictions


def _next_version(name: str) -> int:
    """
    Scans MODELS_DIR for files like '{name}_v<N>_<timestamp>.pkl' and
    returns the next version number to use (1 if none exist yet).
    """
    pattern = os.path.join(MODELS_DIR, f"{name}_v*_*.pkl")
    existing = glob.glob(pattern)
    version_re = re.compile(rf"^{re.escape(name)}_v(\d+)_")

    versions = []
    for path in existing:
        match = version_re.match(os.path.basename(path))
        if match:
            versions.append(int(match.group(1)))

    return max(versions, default=0) + 1


def save_models(models: Dict[str, object]) -> Dict[str, str]:
    """
    Save each trained model to disk with a versioned filename, e.g.
        models/logreg_v1_<timestamp>.pkl
        models/random_forest_v1_<timestamp>.pkl

    Returns:
        dict of model_name -> filepath saved to, so run_pipeline.py can log
        it in run_log.json.

    Raises:
        ValueError: if models is empty.
    """
    if not models:
        raise ValueError("save_models requires a non-empty models dict")

    os.makedirs(MODELS_DIR, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    saved_paths: Dict[str, str] = {}
    for name, model in models.items():
        version = _next_version(name)
        filename = f"{name}_v{version}_{timestamp}.pkl"
        filepath = os.path.join(MODELS_DIR, filename)
        with open(filepath, "wb") as f:
            pickle.dump(model, f)
        saved_paths[name] = filepath

    return saved_paths
"""
models.py
YOUR JOB:
Train and serve the two required classical ML models:
    - Logistic Regression
    - Random Forest Classifier
(Optional stretch: KNN as a 3rd model.)
"""

from typing import Dict, List, Tuple
import os
import pickle
import time


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

    You'll likely use sklearn.linear_model.LogisticRegression and
    sklearn.ensemble.RandomForestClassifier here.
    """
    return {}


def predict(models: Dict[str, object], feature_vector: List[float]) -> Dict[str, int]:
    """
    Get a prediction (0 or 1) from each trained model for one feature vector.

    Args:
        models: dict returned by train_models().
        feature_vector: single feature vector, same order used in training.

    Returns:
        dict like {"logreg": 1, "random_forest": 0}
    """
    return {}


def save_models(models: Dict[str, object]) -> Dict[str, str]:
    """
    Save each trained model to disk with a versioned filename, e.g.
        models/logreg_v1_<timestamp>.pkl
        models/random_forest_v1_<timestamp>.pkl

    Returns:
        dict of model_name -> filepath saved to, so run_pipeline.py can log
        it in run_log.json.
    """
    return {}

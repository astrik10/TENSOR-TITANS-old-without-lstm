"""
features.py
YOUR JOB:
Implement feature computation from a rolling buffer of recent BTC ticks.
A "tick" is a dict like: {"timestamp": "...", "coin": "bitcoin", "price_usd": 61234.5}
The buffer passed in is a list of the most recent N ticks (suggested N=20),
ordered oldest -> newest.
"""

from typing import List, Dict


def compute_features(buffer: List[Dict]) -> Dict[str, float]:
    """
    Compute features for the CURRENT tick (the last item in buffer) using the
    rolling window of ticks that precede it.

    Required features (minimum):
        - rolling_mean_5:  mean price of the last 5 ticks
        - rolling_mean_20: mean price of the last 20 ticks
        - momentum_5:      current price - price 5 ticks ago
        - rolling_vol_10:  std. dev. of price over the last 10 ticks

    Args:
        buffer: list of tick dicts, oldest first, newest last.
                len(buffer) may be less than 20 early on — handle that
                (e.g. by only using as many ticks as are available).

    Returns:
        A dict of feature_name -> float value for the most recent tick.
    """
    return {}


def make_label(buffer: List[Dict], next_tick: Dict) -> int:
    """
    Compute the training label for the tick at buffer[-1]: did price go UP (1)
    or DOWN/SAME (0) on the next tick?

    Args:
        buffer: rolling buffer ending at the tick being labeled.
        next_tick: the tick that came right after buffer[-1].

    Returns:
        1 if next_tick price > buffer[-1] price, else 0.
    """
    return -1

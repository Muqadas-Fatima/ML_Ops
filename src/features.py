
import pandas as pd


def binarize_quality(df: pd.DataFrame) -> pd.Series:
    """
    Convert wine quality into a binary target.

    Quality 7 or higher is labeled as 1 (good),
    while quality below 7 is labeled as 0.
    """
    return (df["quality"] >= 7).astype(int)

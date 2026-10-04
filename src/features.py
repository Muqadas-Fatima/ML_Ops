import pandas as pd


def binarize_quality(df: pd.DataFrame) -> pd.Series:
    """
    Convert wine quality scores into binary quality labels.

    Quality scores of 7 or higher are labeled as 1 (high quality),
    while scores below 7 are labeled as 0 (lower quality).
    """
    return (df["quality"] >= 7).astype(int)



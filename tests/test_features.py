
import pandas as pd

from src.features import binarize_quality


def test_binarize_quality():
    df = pd.DataFrame({
        "quality": [5, 6, 7, 8]
    })

    result = binarize_quality(df)

    expected = pd.Series(
        [0, 0, 1, 1],
        name="quality"
    )

    pd.testing.assert_series_equal(
        result.reset_index(drop=True),
        expected
    )

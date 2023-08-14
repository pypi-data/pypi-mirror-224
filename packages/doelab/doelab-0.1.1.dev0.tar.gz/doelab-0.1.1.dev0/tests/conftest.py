import pytest

import numpy as np
import pandas as pd


@pytest.fixture(scope='module')
def test_L4():
    """
    Set the L4 orthgoonal arrays
    """
    return pd.DataFrame(
        np.array([
            [1, 1, 1],
            [1, 2, 2],
            [2, 1, 2],
            [2, 2, 1]
        ]),
        columns=[f"v{i+1}" for i in range(3)]
    )

@pytest.fixture(scope='module')
def test_L8():
    """
    Set the L8 orthgoonal arrays
    """
    return pd.DataFrame(
        np.array([
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 2, 2, 2, 2],
            [1, 2, 2, 1, 1, 2, 2],
            [1, 2, 2, 2, 2, 1, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 2, 1, 2, 1],
            [2, 2, 1, 1, 2, 2, 1],
            [2, 2, 1, 2, 1, 1, 2]
        ]),
        columns=[f"v{i+1}" for i in range(7)]
    )

@pytest.fixture(scope='module')
def test_L9():
    """
    Set the L9 (3^9) orthgoonal arrays
    """
    return pd.DataFrame(
        np.array([
            [1, 1, 1, 1],
            [1, 2, 2, 2],
            [1, 3, 3, 3],
            [2, 1, 2, 3],
            [2, 2, 3, 1],
            [2, 3, 1, 2],
            [3, 1, 3, 2],
            [3, 2, 1, 3],
            [3, 3, 2, 1]
        ]),
        columns=[f"v{i+1}" for i in range(4)]
    )

"""
test_replication.py

Ensures replicate_table_1 produces the correct results within tolerance.
"""

import pytest
import pandas as pd
import os
from src.replication import replicate_table_1

def test_table_1_replication():
    df_clean = pd.read_csv("data/cleaned/cleaned_data.csv")
    results = replicate_table_1(df_clean)

    # Suppose we want to check the coefficient 'beta' is close to 0.25
    # (Replace with real expected values from the paper)
    expected_beta = 0.25
    tolerance = 0.01
    assert abs(results.get('beta', 0) - expected_beta) < tolerance, "Beta coefficient out of tolerance"

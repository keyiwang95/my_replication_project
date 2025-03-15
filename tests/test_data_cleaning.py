"""
test_data_cleaning.py

Ensures data_cleaning.py produces a properly shaped, tidy dataset.
"""

import os
import pandas as pd

def test_cleaned_data_exists():
    cleaned_file = 'data/cleaned/cleaned_data.csv'
    assert os.path.exists(cleaned_file), "Cleaned data file does not exist."

def test_cleaned_data_shape():
    df = pd.read_csv('data/cleaned/cleaned_data.csv')
    # Example: check that we have the columns we expect
    expected_cols = {'date', 'spot_rate', 'forward_rate'}
    missing_cols = expected_cols - set(df.columns)
    assert not missing_cols, f"Missing columns: {missing_cols}"

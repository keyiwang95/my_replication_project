"""
data_cleaning.py

Reads raw OptionMetrics data from data/raw,
cleans it, and saves a tidy CSV to data/cleaned.
"""

import pandas as pd
import os
from settings import DATA_DIR_RAW, DATA_DIR_CLEANED

def main():
    # Example: read a CSV from data/raw
    # raw_path = os.path.join(DATA_DIR_RAW, 'optionmetrics_raw.csv')
    # data = pd.read_csv(raw_path)

    # Clean / transform data
    # data['date'] = pd.to_datetime(data['date'])
    # data = data.dropna(...)  # etc.

    # Save cleaned data
    cleaned_path = os.path.join(DATA_DIR_CLEANED, 'cleaned_data.csv')
    # data.to_csv(cleaned_path, index=False)
    pass

if __name__ == "__main__":
    main()

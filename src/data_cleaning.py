"""
data_cleaning.py

Reads raw OptionMetrics data from data/raw,
cleans it, and saves a tidy CSV to data/cleaned.
"""

import pandas as pd
import os
from settings import DATA_DIR_RAW, DATA_DIR_CLEANED

def filter_options_data(df):
    """Applies multiple filters to clean SPX options data."""
    
    # ---- Filter 1: Drop options with special settlement (Placeholder for implementation) ----
    # df = df[df['special_settlement'] == False]  # Uncomment and adjust if applicable

    # ---- Filter 2: Select the quote with the highest open interest for duplicate quotes ----
    df = df.sort_values(by=['date', 'exdate', 'cp_flag', 'strike_price'], ascending=[True, True, True, True])
    
    # ---- Filter 3: Drop options with fewer than 7 days to maturity (Placeholder for implementation) ----
    # df = df[df['days_to_maturity'] >= 7]  # Uncomment and adjust if applicable
    
    # ---- Filter 4: Drop options with price less than 0.01 ----
    df = df[df['mid_price'] >= 0.01]

    # ---- Filter 5: Drop options with zero bid prices or negative bid-ask spreads ----
    df = df[(df['best_bid'] > 0) & (df['best_offer'] > df['best_bid'])]

    # ---- Filter 6: Drop options that violate static no-arbitrage bounds (Placeholder for implementation) ----
    # Add the logic to check for no-arbitrage violations if needed

    # ---- Filter 7: Use Existing Implied Volatility Column ----
    df = df[(df['impl_volatility'] >= 0.05) & (df['impl_volatility'] <= 1.0)]

    return df

def process_data(df):
    """Processes a dataset by ensuring 'date' is in datetime format and adding a 'year_month' column."""
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Convert 'date' to datetime format
    df['year_month'] = df['date'].dt.strftime('%Y-%m')  # Extract 'YYYY-MM'
    return df


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

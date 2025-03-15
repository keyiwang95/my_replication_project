"""
generate_figures_tables.py

Uses the cleaned data (potentially extended with new time periods)
to produce updated versions of Table 1 and Figure 1.
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from settings import DATA_DIR_CLEANED, OUTPUTS_DIR

def generate_updated_table_1(df_clean):
    # Compute stats for an updated date range
    results = {}
    return results

def generate_updated_figure_1(df_clean):
    fig, ax = plt.subplots()
    # ...
    fig_path = os.path.join(OUTPUTS_DIR, 'figure1_updated.png')
    plt.savefig(fig_path, dpi=300)
    plt.close()

def main():
    df_clean = pd.read_csv(os.path.join(DATA_DIR_CLEANED, 'cleaned_data.csv'))
    # Maybe filter to a new date range:
    # df_updated = df_clean[df_clean['date'] >= '2020-01-01']

    updated_table1 = generate_updated_table_1(df_clean)
    pd.DataFrame([updated_table1]).to_csv(os.path.join(OUTPUTS_DIR, 'table1_updated.csv'), index=False)

    generate_updated_figure_1(df_clean)

if __name__ == "__main__":
    main()

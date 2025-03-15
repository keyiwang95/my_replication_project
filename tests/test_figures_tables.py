"""
test_figures_tables.py

Tests that figure generation code runs without errors.
"""

import os
import pandas as pd
from src.replication import replicate_figure_1

def test_figure_1_generation():
    df_clean = pd.read_csv("data/cleaned/cleaned_data.csv")
    replicate_figure_1(df_clean)
    assert os.path.exists('outputs/figure1_replication.png'), "Figure 1 PNG not generated."

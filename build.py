"""
build.py

Defines PyDoit tasks to automate the project workflow:
1. Clean raw data
2. Replicate original table/figures
3. Generate updated table/figures
4. Build LaTeX report
5. Run tests
"""

import os
from doit.tools import create_folder, LongRunning

def task_clean_data():
    """Clean the raw data and save to data/cleaned."""
    return {
        'actions': [
            'python src/data_cleaning.py'
        ],
        'targets': ['data/cleaned/cleaned_data.csv'],
        'file_dep': ['data/raw/some_file.csv'],  # or however your raw data is stored
        'clean': True
    }

def task_replicate_results():
    """Replicate Table 1 and Figure 1 from the paper."""
    return {
        'actions': [
            'python src/replication.py'
        ],
        'file_dep': ['data/cleaned/cleaned_data.csv'],
        'targets': [
            'outputs/table1_replication.csv',
            'outputs/figure1_replication.png'
        ],
        'clean': True
    }

def task_generate_updated_results():
    """Generate updated Table 1 and Figure 1 with more recent data."""
    return {
        'actions': [
            'python src/generate_figures_tables.py'
        ],
        'file_dep': ['data/cleaned/cleaned_data.csv'],
        'targets': [
            'outputs/table1_updated.csv',
            'outputs/figure1_updated.png'
        ],
        'clean': True
    }

def task_build_latex():
    """Build the final LaTeX report containing all tables/figures."""
    return {
        'actions': [
            'pdflatex -interaction=nonstopmode report.tex'
        ],
        'file_dep': [
            'report.tex',
            'outputs/table1_replication.csv',
            'outputs/figure1_replication.png',
            # add more dependencies if needed
        ],
        'targets': ['report.pdf'],
        'clean': True
    }

def task_test():
    """Run all unit tests with pytest."""
    return {
        'actions': [
            LongRunning('pytest tests')
        ],
        'file_dep': []
    }

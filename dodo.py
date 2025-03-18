from doit import create_after

def task_process_data():
    """Task to process data using main.py"""
    return {
        'actions': ['python src/main.py'],
        'file_dep': ['src/main.py', 'src/data_processing.py'],
        'targets': ['SPX_Options_Monthly.csv', 'SP500_index_monthly.csv'],
        'verbosity': 2
    }

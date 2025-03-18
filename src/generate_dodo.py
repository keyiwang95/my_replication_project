import os

# Get the root directory (one level up from the current script's location)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

dodo_content = """\
from doit import create_after

def task_process_data():
    \"\"\"Task to process data using main.py\"\"\"
    return {
        'actions': ['python src/main.py'],
        'file_dep': ['src/main.py', 'src/data_processing.py'],
        'targets': ['SPX_Options_Monthly.csv', 'SP500_index_monthly.csv'],
        'verbosity': 2
    }
"""

# Write dodo.py to the root directory
with open(os.path.join(root_dir, "dodo.py"), "w") as f:
    f.write(dodo_content)

print(f"✅ dodo.py has been generated successfully in {root_dir}!")
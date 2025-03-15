"""
settings.py

Holds default settings for the project.
Loads environment variables if present.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env if it exists
load_dotenv()

# Directories
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATA_DIR_RAW = os.getenv("DATA_DIR_RAW", os.path.join(PROJECT_ROOT, "data", "raw"))
DATA_DIR_CLEANED = os.getenv("DATA_DIR_CLEANED", os.path.join(PROJECT_ROOT, "data", "cleaned"))
OUTPUTS_DIR = os.getenv("OUTPUTS_DIR", os.path.join(PROJECT_ROOT, "outputs"))

# Date range
START_DATE = os.getenv("START_DATE", "1996-01-01")
END_DATE = os.getenv("END_DATE", "2025-12-31")

# WRDS credentials
WRDS_USERNAME = os.getenv("WRDS_USERNAME", "your_wrds_username")
WRDS_PASSWORD = os.getenv("WRDS_PASSWORD", "")

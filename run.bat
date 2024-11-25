#!/bin/bash
# Activate virtual environment
source .venv/bin/activate

# Run pytest with specific options
pytest -s -v -m "sanity"

# Pause to view output
read -p "Press Enter to continue..."

#!/usr/bin/env bash
set -euo pipefail

echo "Project NEURA - environment setup"

python3.11 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pip install -e .
python -m ipykernel install --user --name project-neura --display-name "Python (Project NEURA)"

echo
echo "Environment ready."
echo "Activate with: source .venv/bin/activate"
echo "Launch notebooks with: jupyter lab"
echo "Optional neuro stack: python -m pip install -r requirements-neuro.txt"

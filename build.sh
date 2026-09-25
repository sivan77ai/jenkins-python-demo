#!/usr/bin/env bash
# Build script used by the Jenkins job.
# -e  : stop on the first failing command
# -u  : treat unset variables as an error
# -o pipefail : a failing command in a pipeline fails the whole pipeline
set -euo pipefail

echo "=== Python version ==="
python3 --version

echo "=== Creating virtual environment ==="
python3 -m venv .venv
source .venv/bin/activate

echo "=== Installing dependencies ==="
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

echo "=== Running tests ==="
pytest --junitxml=test-results/results.xml -v

echo "=== Build finished successfully ==="

# jenkins-python-demo

A small Python project for practising CI with Jenkins.

## What's inside

| Path | Purpose |
|------|---------|
| `src/calculator.py` | The code under test: add, subtract, multiply, divide, average |
| `tests/test_calculator.py` | 12 pytest tests, including error cases |
| `requirements.txt` | Dependencies (pytest) |
| `build.sh` | The commands Jenkins runs: venv, install, test |
| `Jenkinsfile` | Declarative pipeline (used from Module 5) |
| `pytest.ini` | Tells pytest where the tests live |

## Run it locally

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Run it the way Jenkins does

```bash
./build.sh
```

## Breaking a test on purpose

To see a red build in Jenkins, change `add` in `src/calculator.py`:

```python
def add(a, b):
    return a - b        # deliberate bug
```

Commit, push, and build again. Several tests fail and Jenkins marks the build
as FAILURE. Change it back to `a + b` to go green again.

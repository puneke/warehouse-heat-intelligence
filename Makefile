.PHONY: check-data preprocess analysis notebooks

PYTHON := $(shell if [ -x .venv/bin/python ]; then echo .venv/bin/python; else command -v python3; fi)

check-data:
	$(PYTHON) scripts/check_data.py

preprocess:
	$(PYTHON) scripts/preprocess.py

analysis:
	$(PYTHON) scripts/run_notebooks.py

notebooks: analysis

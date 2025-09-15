.PHONY: setup-python run-marimo

# venv activate path different for Windows and Unix/Linux environments
#  Windows: source virtual_folder_path/Scripts/activate
#  *nix:    source/bin/activate

setup-python:
	python -m venv venv_marimo_salesforce && \
	source venv_marimo_salesforce/Scripts/activate && \
	pip install -r requirements.txt

run-marimo:
	source venv_marimo_salesforce/Scripts/activate && \
	TOKENIZERS_PARALLELISM=false marimo edit marimo_salesforce_with_duckdb.py
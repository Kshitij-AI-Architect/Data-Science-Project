# End to End DSProject

An end-to-end MLOps project scaffold for building, training, evaluating, and deploying machine learning models.

**Status:** Development

---

**Contents**
- **Purpose:** Provide a reproducible pipeline for ingesting data, validating and transforming it, training models, and evaluating results.
- **Primary files:** `main.py`, `params.yaml`, `config/config.yaml`, `schema.yaml`, `requirements.txt`, `Dockerfile`.
- **Code:** `src/` contains modular components, configuration, entities, utilities, and pipeline code.

---

**Quick Start (Windows PowerShell)**

- Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Install dependencies:

```powershell
pip install -r requirements.txt
```

- Run the full pipeline:

```powershell
python main.py
```

Notes:
- If you use a different Python executable, replace `python` with your Python path.
- Use `pip install --upgrade pip` if dependency installation fails.

---

**Project Structure (high level)**

- `src/` — project source code
	- `datascience/components/` — modular components (data ingestion, validation, transformation, training, evaluation)
	- `datascience/config/` — configuration loader and `ConfigurationManager`
	- `datascience/entity/` — config dataclasses (e.g., `DataIngestionConfig`, `ModelTrainerConfig`)
	- `datascience/utils/` — helpers (`common.py` for YAML/JSON read-write, file ops)
	- `datascience/logging/` — logging utilities
- `config/` — default configuration files (`config.yaml`)
- `params.yaml` — model and training hyperparameters
- `schema.yaml` — expected schema for training data validation
- `research/` — notebooks and experiments
- `templates/` — example templates (e.g., `index.html`)

---

**Configuration**

- Edit `config/config.yaml` to point to artifact directories, data sources, and other environment-specific settings.
- Use `params.yaml` to set model hyperparameters (e.g., test size, random seed, model-specific params).
- `schema.yaml` defines expected columns and types for input data to support the Data Validation step.

**Common workflow**

1. Update `config/config.yaml` and `params.yaml` to your environment and model choices.
2. Run `python main.py` to execute the pipeline steps in order:
	 - Data Ingestion
	 - Data Validation
	 - Data Transformation
	 - Model Training
	 - Model Evaluation
3. Check the `logs/` directory for run logs and `artifacts/` (or configured artifact directories) for outputs.

---

**Development tips**

- Use the notebooks in `research/` for exploratory data analysis and prototyping.
- Keep configuration and parameters outside source code to ensure reproducibility.
- Add new pipeline components as modules under `src/datascience/components/` and register them in the pipeline if needed.

**Testing changes locally**

- Run individual module-level checks in an interactive console, for example:

```powershell
python -c "from src.datascience.utils.common import read_yaml; print(read_yaml('config/config.yaml'))"
```

---

**Optional: Use Docker**

- Build the image (if a `Dockerfile` is present):

```powershell
docker build -t kshitij-dsproject .
```

- Run the image (adjust volumes/env as needed):

```powershell
docker run --rm -v ${PWD}:/app kshitij-dsproject python main.py
```

---

**Troubleshooting**

- If imports fail, ensure the project root is on `PYTHONPATH` or install the package in editable mode:

```powershell
pip install -e .
```

- If a dependency is missing, install it using `pip install <package>` and consider adding it to `requirements.txt`.

## End to end machine learning project for Data Science
# Workflows -- ML Pipeline
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation

# Workflow Steps
1. Update config.yaml - Some basic configurations that we require
2. Update schema.yaml - To check the schema of data we get from data ingestion for data validation step
3. Update params.yaml - For providing model parameters
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py

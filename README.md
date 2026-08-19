# Project NEURA

**Biological Intelligence Research & Neural Data Computing**

Project NEURA is a research project by **Beyond Geeks & Voyage** focused on studying biological neuronal activity using software, data analysis, signal processing, and machine learning.

The project starts with existing neuronal recordings instead of growing or working directly with biological tissue.

## Current Phase

We are currently in **Phase 0 — Data Exploration**.

The first goal is to understand the neuronal datasets we receive and build tools that can analyse them.

We will initially explore:

* neuronal activity across different channels;
* spike and firing patterns;
* changes in activity over time;
* noise and signal quality;
* synchronisation between channels;
* recurring activity patterns;
* unusual or abnormal activity;
* visualisation of neuronal recordings;
* machine-learning experiments based on the recorded activity.

## Project Scope

Project NEURA is currently focused on the **software and data side of neuroscience research**.

We are not currently growing neurons, culturing biological tissue, or performing wet-lab experiments.

Our work focuses on analysing neuronal recordings provided by research organisations and building software that helps us understand the data.

## FinalSpark Dataset

Project NEURA will initially work with neuronal activity data provided by **FinalSpark**.

FinalSpark will be credited as the data source in any research, presentation, publication, or public work that uses their dataset.

Raw FinalSpark data will **not be uploaded to this public repository**.

The dataset should remain stored locally inside:

`data/raw/`

and is excluded from Git.

## Repository Structure

```text
PROJECT_NEURA/
├── config/
├── data/
├── docs/
├── notebooks/
├── scripts/
├── src/
└── tests/
```

## Getting Started — Windows

```powershell
git clone https://github.com/BeyondGeeksKe/PROJECT_NEURA.git
cd PROJECT_NEURA

Set-ExecutionPolicy -Scope Process Bypass

.\scripts\setup.ps1

.\.venv\Scripts\Activate.ps1

jupyter lab
```

## Getting Started — Linux/macOS

```bash
git clone https://github.com/BeyondGeeksKe/PROJECT_NEURA.git

cd PROJECT_NEURA

chmod +x scripts/setup.sh

./scripts/setup.sh

source .venv/bin/activate

jupyter lab
```

## Optional Neuroscience Tools

Once we understand the exact format of the FinalSpark dataset, additional neuroscience tools can be installed using:

```bash
python -m pip install -r requirements-neuro.txt
```

## First Notebook

Start with:

`notebooks/00_environment_check.ipynb`

This checks that the local environment is working correctly.

Once the neuronal dataset is available, continue with:

`notebooks/01_explore_recording.ipynb`

This will be used to begin exploring the recordings.

## Data Rules

Do not upload:

* raw FinalSpark datasets;
* private research data;
* passwords;
* API keys;
* access tokens;
* private download links.

More information is available in:

`docs/data-ethics.md`

## Status

Project NEURA is currently in its early research stage.

The project structure, analysis methods, and tools will continue to develop as we begin working with real neuronal recordings.

## Organisation

**Beyond Geeks & Voyage**

https://beyondgeeksandvoyage.com

GitHub:

https://github.com/BeyondGeeksKe/PROJECT_NEURA

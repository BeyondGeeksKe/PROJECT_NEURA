# Project NEURA

**Biological Intelligence Research & Neural Data Computing**

Project NEURA is an experimental research initiative by **Beyond Geeks & Voyage** exploring the computational analysis of biological neuronal activity.

The project begins on the software, infrastructure, signal-processing and data-analysis side: working with electrophysiological recordings from living neuronal systems and building reproducible pipelines for inspection, preprocessing, spike/activity analysis, visualisation and machine-learning experiments.

## Current phase

**Phase 0 — Data intake and exploratory analysis**

Initial work is focused on understanding the structure, scale and characteristics of research datasets such as neuronal recordings made available by FinalSpark.

Planned early work includes:

- dataset inventory and metadata inspection;
- channel/electrode signal visualisation;
- quality and noise checks;
- spike/event exploration;
- firing-rate and inter-spike-interval analysis;
- cross-channel synchronisation and correlation;
- recurring-pattern and anomaly exploration;
- reproducible experiment notebooks.

## Research positioning

Project NEURA is currently a computational research project. It does **not** grow, culture or directly stimulate biological neural tissue. The initial work is deliberately focused on software engineering, data infrastructure and analysis of supplied research recordings.

## FinalSpark data

FinalSpark states that its Neuroplatform records electrophysiological activity continuously and provides Python-based research tooling. FinalSpark also makes recorded neuronal activity data available to researchers.

**Important:** raw FinalSpark data is not stored in this repository. Third-party datasets should be kept locally under `data/raw/` and remain excluded from Git.

Any publication, presentation, research output or public result derived from FinalSpark-provided data should appropriately cite **FinalSpark** as the data source and follow any additional terms supplied with the dataset.

## Repository layout

```text
project-neura/
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── derived/
├── docs/
├── notebooks/
├── scripts/
├── src/neura/
└── tests/
```

## Quick start — Windows PowerShell

```powershell
git clone <YOUR_REPOSITORY_URL>
cd project-neura
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
jupyter lab
```

## Quick start — Linux/macOS

```bash
git clone <YOUR_REPOSITORY_URL>
cd project-neura
chmod +x scripts/setup.sh
./scripts/setup.sh
source .venv/bin/activate
jupyter lab
```

The default environment stays deliberately lightweight. Once the exact FinalSpark dataset format is known, install the optional electrophysiology stack:

```bash
python -m pip install -r requirements-neuro.txt
```

## First notebook

Open:

`notebooks/00_environment_check.ipynb`

Then, after the dataset arrives, begin with:

`notebooks/01_explore_recording.ipynb`

## Data policy

Do not commit raw third-party recordings, credentials, access tokens or restricted research material. See [`docs/data-ethics.md`](docs/data-ethics.md).

## Status

Early research scaffold. Interfaces and analysis methods will change as the first dataset is inspected.

## Organisation

**Beyond Geeks & Voyage**  
https://beyondgeeksandvoyage.com

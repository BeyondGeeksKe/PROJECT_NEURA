<div align="center">

# 🧠 PROJECT NEURA

### `Biological Intelligence Research // Neural Data Computing`

**What happens when software starts listening to living neurons?**

```text
neurons → signals → data → patterns → questions
```

A research project by **Beyond Geeks & Voyage**.

</div>

---

## `> what_is_neura?`

**Project NEURA** is an experimental research project exploring biological neuronal activity through:

* software engineering;
* data analysis;
* signal processing;
* visualisation;
* machine learning.

The idea is simple:

> Before trying to build anything with biological intelligence,
> we first need to understand the signals it produces.

So that is where we are starting.

NEURA begins entirely on the **software and data side**.

No neuron culturing.

No wet lab.

No biological tissue handling.

For now, just data, code and a lot of questions.

---

## `> current_phase`

```yaml
project: NEURA
phase: 0
name: Data Exploration
status: early_research
wet_lab: false
neurons_grown_by_us: 0
questions: many
```

We are currently in:

### **Phase 0 — Data Exploration**

Before building complicated models, we need to understand the recordings themselves.

Our first objective is to create a reliable pipeline for loading, inspecting, cleaning, visualising and analysing neuronal recordings.

---

## `> what_are_we_looking_for?`

At this stage, we are exploring things like:

```text
signal
 ├── activity across channels
 ├── spike detection
 ├── firing patterns
 ├── signal quality
 ├── noise
 ├── changes over time
 ├── synchronisation
 ├── recurring patterns
 ├── unusual activity
 └── machine-learning representations
```

In simpler terms:

**What are the neurons doing?**

**When are they doing it?**

**Are different neurons doing something together?**

**Do certain patterns repeat?**

**Can software learn to recognise those patterns?**

Those questions come before any bigger claims.

---

## `> scope`

NEURA currently focuses on the computational side of neuroscience research.

Our work includes:

* processing neuronal recordings;
* analysing time-series neural signals;
* detecting neuronal spikes;
* measuring firing behaviour;
* comparing activity between channels;
* studying synchronisation;
* identifying recurring patterns;
* detecting unusual activity;
* creating visualisations;
* experimenting with machine-learning methods.

### What NEURA is **not** currently doing

We are **not**:

* growing neurons;
* culturing biological tissue;
* performing wet-lab experiments;
* manufacturing biological computers;
* claiming to have created biological intelligence.

We are starting with what we know:

```text
software + infrastructure + data
```

And learning from there.

---

## `> data_source`

### FinalSpark

One of the initial data sources planned for Project NEURA is neuronal activity data from **FinalSpark**.

Where FinalSpark data is used, **FinalSpark will be credited as the source** in research, presentations, publications and other public work produced from that dataset.

Raw research data does **not** belong in this public repository.

```text
public_repository/
    ❌ raw neural datasets

local_environment/
    ✅ data/raw/
```

Raw datasets should remain inside:

```text
data/raw/
```

This directory is excluded from Git.

Access restrictions and terms attached to research datasets must always be respected.

---

## `> tree PROJECT_NEURA/`

```text
PROJECT_NEURA/
│
├── config/       # project configuration
├── data/         # local datasets and processed data
├── docs/         # research notes and documentation
├── notebooks/    # exploration and experiments
├── scripts/      # setup and utility scripts
├── src/          # reusable NEURA code
└── tests/        # because research code can break too
```

---

# `> boot_neura`

## Windows

Clone the repository:

```powershell
git clone https://github.com/BeyondGeeksKe/PROJECT_NEURA.git
cd PROJECT_NEURA
```

Allow the setup script for the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

Run setup:

```powershell
.\scripts\setup.ps1
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Launch Jupyter:

```powershell
jupyter lab
```

---

## Linux / macOS

Clone the repository:

```bash
git clone https://github.com/BeyondGeeksKe/PROJECT_NEURA.git
cd PROJECT_NEURA
```

Make the setup script executable:

```bash
chmod +x scripts/setup.sh
```

Run it:

```bash
./scripts/setup.sh
```

Activate the environment:

```bash
source .venv/bin/activate
```

Launch Jupyter:

```bash
jupyter lab
```

---

## `> optional_neuro_tools`

We are intentionally keeping the starting environment simple.

Once the structure and format of the neuronal datasets are understood, additional neuroscience libraries can be installed with:

```bash
python -m pip install -r requirements-neuro.txt
```

No point installing half the neuroscience ecosystem before we know what we actually need.

---

## `> start_here`

### 01 — Environment Check

Start with:

```text
notebooks/00_environment_check.ipynb
```

This answers the first and most important question:

```text
does_the_environment_work == True ?
```

It verifies that Python and the required project dependencies are working correctly.

---

### 02 — Explore a Recording

Once neuronal data is available:

```text
notebooks/01_explore_recording.ipynb
```

This notebook begins the actual exploration of neuronal recordings.

The early workflow will roughly look like:

```text
LOAD
  ↓
INSPECT
  ↓
CLEAN
  ↓
VISUALISE
  ↓
MEASURE
  ↓
FIND PATTERNS
  ↓
ASK BETTER QUESTIONS
```

---

## `> data_rules`

Research data needs to be treated carefully.

Never commit:

```text
❌ raw FinalSpark datasets
❌ private research datasets
❌ passwords
❌ API keys
❌ access tokens
❌ private download links
❌ credentials
```

More information:

```text
docs/data-ethics.md
```

When unsure:

```python
if data_is_private:
    git_commit = False
```

---

## `> where_is_this_going?`

NEURA is deliberately starting small.

Phase 0 is not about making huge claims about biological computing.

It is about building the foundation required to investigate it properly.

Today:

```text
recordings → analysis → understanding
```

Later, those foundations may allow us to investigate bigger questions around:

```text
biological neural behaviour
        ↓
machine learning
        ↓
computational representations
        ↓
biological intelligence
        ↓
?
```

We don't know exactly where that road ends.

That is partly the point.

---

## `> research_principle`

```text
Don't force the data to tell an exciting story.

Understand what it actually says.
```

NEURA is an experiment before it is a product.

Some ideas will work.

Some won't.

Both outcomes are useful.

---

## `> status`

```yaml
name: Project NEURA
organisation: Beyond Geeks & Voyage
phase: 0
focus: neural_data_exploration
research: active
production_system: false
biological_lab: false
next_step: understand_the_data
```

---

## `> organisation`

**Beyond Geeks & Voyage**

🌐 [beyondgeeksandvoyage.com](https://beyondgeeksandvoyage.com)

💻 [github.com/BeyondGeeksKe](https://github.com/BeyondGeeksKe)

Repository:

**[BeyondGeeksKe/PROJECT_NEURA](https://github.com/BeyondGeeksKe/PROJECT_NEURA)**

---

<div align="center">

### `signal → pattern → understanding → ?`

**PROJECT NEURA**

*We don't know what we'll find yet.*

*That's why we're looking.*

🧠 × 🦉

**Beyond Geeks & Voyage**

</div>

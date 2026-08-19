$ErrorActionPreference = "Stop"

Write-Host "Project NEURA - Windows environment setup"

$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) {
    py -3.11 -m venv .venv
} else {
    python -m venv .venv
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
& .\.venv\Scripts\python.exe -m pip install -e .
& .\.venv\Scripts\python.exe -m ipykernel install --user --name project-neura --display-name "Python (Project NEURA)"

Write-Host ""
Write-Host "Environment ready."
Write-Host "Activate with: .\.venv\Scripts\Activate.ps1"
Write-Host "Launch notebooks with: jupyter lab"
Write-Host "Optional neuro stack: python -m pip install -r requirements-neuro.txt"

"""
Generar casos de prueba, en formato JSON, para el ejercicio.
"""

import json
from pathlib import Path

PROG = "boda.py"

base_dir = Path(".")
tests_file = base_dir / "solution" / "test_cases.json"
input_folder = base_dir / "solution" / "input"
output_folder = base_dir / "solution" / "output"

output = {}
tests = []

for f in input_folder.glob("*"):
    inp = f.read_text()
    outp = (output_folder / f.name).read_text()
    name = f"{f.name}"
    entry = {
        "name": name,
        "type": "io",
        "run": "python3 " + PROG,
        "points": 1,
        "comparison": "exact",
        "input": inp,
        "expected": outp,
        }
    tests.append(entry)

# Añadir sangrías extra para copiar en archivo de Classroom 50
clsrm50 = {"assignments": [{"tests": tests}]}

with tests_file.open("w", encoding="utf-8") as f:
    json.dump(clsrm50, f, indent=2, ensure_ascii=False)

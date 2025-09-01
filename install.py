import os
import subprocess
import sys

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.check_call(cmd, shell=True)

venv_dir = ".venv"
if not os.path.exists(venv_dir):
    run(f"{sys.executable} -m venv {venv_dir}")

if os.name == "nt":
    python_bin = os.path.join(venv_dir, "Scripts", "python.exe")
    pip_bin = os.path.join(venv_dir, "Scripts", "pip.exe")
else:
    python_bin = os.path.join(venv_dir, "bin", "python")
    pip_bin = os.path.join(venv_dir, "bin", "pip")

run(f"{python_bin} -m pip install --upgrade pip")

run(f"{pip_bin} install fugashi unidic-lite")

run(f"{pip_bin} install -r requirements.txt")

print("Installed! Ready to work.")

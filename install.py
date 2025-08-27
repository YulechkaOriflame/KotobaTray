import subprocess
import sys
import os

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.check_call(cmd, shell=True)

# 1. Создаём виртуальное окружение, если нет
venv_dir = ".venv"
if not os.path.exists(venv_dir):
    run(f"{sys.executable} -m venv {venv_dir}")

# 2. Определяем путь к pip и python в виртуальном окружении
if os.name == "nt":
    # Windows
    python_bin = os.path.join(venv_dir, "Scripts", "python.exe")
    pip_bin = os.path.join(venv_dir, "Scripts", "pip.exe")
else:
    # macOS / Linux
    python_bin = os.path.join(venv_dir, "bin", "python")
    pip_bin = os.path.join(venv_dir, "bin", "pip")

# 3. Обновляем pip
run(f"{python_bin} -m pip install --upgrade pip")

# 4. Ставим зависимости
run(f"{pip_bin} install -r requirements.txt")

# 5. Скачиваем словарь UniDic
run(f"{python_bin} -m unidic download")

print("Установка завершена! Виртуальное окружение готово к работе.")

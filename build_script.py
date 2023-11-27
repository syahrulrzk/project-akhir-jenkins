# build_script.py
import subprocess
import sys

def install_dependencies():
    try:
        print("Installing dependencies...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        subprocess.run(["venv/bin/python", "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def build_project():
    try:
        print("Building the Python project...")
        # Add additional build steps as needed
        print("Build completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
    build_project()

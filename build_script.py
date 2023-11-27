# build_script.py

import subprocess
import sys
import os
import shutil

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
        # Add your build steps here

        # Create a 'build' directory if not exists
        os.makedirs("build", exist_ok=True)

        # Copy or move the build artifacts to the 'build' directory
        shutil.copytree(".", "build/")  # Assuming build artifacts are in the same directory
        print("Build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    install_dependencies()
    build_project()

if __name__ == "__main__":
    main()

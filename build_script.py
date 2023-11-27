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

        # Check if 'build' directory already exists
        if not os.path.exists("build"):
            os.makedirs("build")
        else:
            print("'build' directory already exists. Removing its contents.")
            # Clear the contents of the 'build' directory if it already exists
            shutil.rmtree("build")
            os.makedirs("build")

        # Copy or move the build artifacts to the 'build' directory
        for item in os.listdir("."):
            if item != "build":  # Exclude the 'build' directory
                shutil.copy(item, os.path.join("build", item))

        print("Build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    install_dependencies()
    build_project()

if __name__ == "__main__":
    main()

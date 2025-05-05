#!/usr/bin/env python
"""
Render setup script to install additional dependencies
"""
import subprocess
import sys
import os

def install_dependencies():
    """Install dependencies using pinned requirements file"""
    print("Installing dependencies from requirements-render.txt...")
    
    requirements_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements-render.txt")
    
    try:
        # Using --no-deps speeds up installation by skipping dependency resolution
        # Using --no-build-isolation can speed up the process further
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "-r", requirements_path,
            "--no-deps",  # Skip dependency resolution to speed up installation
            "--no-build-isolation"  # Speed up build further
        ])
        print("Successfully installed dependencies from requirements-render.txt")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        # Fall back to individual installations if the requirements file approach fails
        install_individual_deps()

def install_individual_deps():
    """Fall back to installing individual dependencies if the requirements file fails"""
    DEPENDENCIES = [
        "openai",
        "fastapi",
        "uvicorn",
        "langchain",
        "langchain-openai",
        "pydantic",
        "httpx",
        "python-multipart",
        "langchain-google-community",
        "astrapy",
        "toml",
        "gitpython",
        "langflow"
    ]
    
    print("Falling back to individual dependency installation...")
    for dep in DEPENDENCIES:
        print(f"Installing {dep}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep, "--no-deps"])
            print(f"Successfully installed {dep}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {dep}")

if __name__ == "__main__":
    install_dependencies()

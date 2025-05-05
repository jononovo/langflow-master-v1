#!/usr/bin/env python
"""
Render setup script to install additional dependencies
"""
import subprocess
import sys

# Dependencies that might be missing
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

def install_dependencies():
    """Install missing dependencies"""
    print("Installing additional dependencies...")
    for dep in DEPENDENCIES:
        print(f"Installing {dep}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"Successfully installed {dep}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {dep}")
    
    print("All additional dependencies installed.")

if __name__ == "__main__":
    install_dependencies()

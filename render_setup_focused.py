#!/usr/bin/env python
"""
Focused Render setup script - installs only the dependencies needed for specific features
"""
import subprocess
import sys
import os
import time

def install_dependencies():
    """Install dependencies using the focused requirements file"""
    start_time = time.time()
    print("Installing focused dependencies...")
    
    requirements_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements-focused.txt")
    
    try:
        # Install langflow package from the backend/base directory
        backend_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "backend", "base")
        print(f"Installing langflow from {backend_base_path}")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-e", backend_base_path
        ])
        print("Successfully installed langflow package")
        
        # Install dependencies from the focused requirements file
        print(f"Installing dependencies from {requirements_path}")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "-r", requirements_path,
            "--no-deps"  # Skip dependency resolution to speed up installation
        ])
        print("Successfully installed focused dependencies")
        
        end_time = time.time()
        print(f"Total installation time: {end_time - start_time:.2f} seconds")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = install_dependencies()
    sys.exit(0 if success else 1)

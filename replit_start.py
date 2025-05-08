#!/usr/bin/env python
"""
Replit startup script for Langflow with focused dependencies
"""
import os
import sys
import subprocess
import time

def install_dependencies():
    """Install the focused dependencies"""
    print("Installing Langflow and dependencies...")
    
    # Install langflow package from the backend/base directory
    backend_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "backend", "base")
    print(f"Installing langflow from {backend_base_path}")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-e", backend_base_path
    ])
    
    # Install dependencies from the focused requirements file
    requirements_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements-focused.txt")
    print(f"Installing dependencies from {requirements_path}")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-r", requirements_path
    ])
    
    print("Successfully installed Langflow and dependencies")
    return True

def run_langflow():
    """Start the Langflow application"""
    # Add backend/base to Python path
    backend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "backend", "base")
    sys.path.append(backend_path)
    
    # Import after path setup
    from langflow.main import create_app
    from fastapi.staticfiles import StaticFiles
    import uvicorn
    from pathlib import Path
    
    # Get port from environment with fallback
    port = int(os.environ.get("PORT", os.environ.get("REPL_PORT", 8080)))
    host = os.environ.get("LANGFLOW_HOST", "0.0.0.0")
    
    print(f"Starting Langflow on {host}:{port}")
    
    # Check if frontend build exists
    frontend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "frontend", "build")
    frontend_exists = os.path.exists(frontend_path)
    
    print(f"Frontend path: {frontend_path}")
    print(f"Frontend exists: {frontend_exists}")
    
    # Create the application
    app = create_app()
    
    # Setup static files explicitly
    if frontend_exists:
        print(f"Setting up static files from: {frontend_path}")
        try:
            # Use FastAPI's StaticFiles
            static_files_dir = Path(frontend_path)
            app.mount("/", StaticFiles(directory=str(static_files_dir), html=True), name="static")
        except Exception as e:
            print(f"Error mounting static files: {e}")
    
    # Run the app with explicit host and port
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level=os.environ.get("LANGFLOW_LOG_LEVEL", "info").lower()
    )

if __name__ == "__main__":
    # First install dependencies
    install_dependencies()
    
    # Then run the application
    run_langflow()

#!/usr/bin/env python
"""
Render startup script for Langflow
"""
import os
import sys
import uvicorn
from pathlib import Path

def main():
    """Start the Langflow application with proper settings for Render"""
    # Add backend/base to Python path
    backend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "backend", "base")
    sys.path.append(backend_path)
    
    # Import after path setup
    from langflow.main import create_app, setup_static_files
    from fastapi.staticfiles import StaticFiles
    
    # Get port from environment with fallback
    port = int(os.environ.get("PORT", os.environ.get("LANGFLOW_PORT", 10000)))
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
            # Use FastAPI's StaticFiles instead of uvicorn's
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
    main()

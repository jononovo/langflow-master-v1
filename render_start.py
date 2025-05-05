#!/usr/bin/env python
"""
Render startup script for Langflow
"""
import os
import sys
import uvicorn

def main():
    """Start the Langflow application with proper settings for Render"""
    # Add backend/base to Python path
    backend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "backend", "base")
    sys.path.append(backend_path)
    
    # Import after path setup
    from langflow.main import create_app
    
    # Get port from environment with fallback
    port = int(os.environ.get("PORT", os.environ.get("LANGFLOW_PORT", 8080)))
    host = os.environ.get("LANGFLOW_HOST", "0.0.0.0")
    
    print(f"Starting Langflow on {host}:{port}")
    
    # Run the app with explicit host and port
    uvicorn.run(
        create_app(),
        host=host,
        port=port,
        log_level=os.environ.get("LANGFLOW_LOG_LEVEL", "info").lower()
    )

if __name__ == "__main__":
    main()

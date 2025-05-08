#!/usr/bin/env python
"""
Replit startup script for Langflow with focused dependencies
"""
import os
import sys
import subprocess
import time

def install_core_dependencies():
    """Install core dependencies one by one to avoid package manager issues"""
    print("Installing core dependencies...")
    
    core_packages = [
        "fastapi>=0.100.0", "uvicorn>=0.20.0", "pydantic>=2.0.0",
        "httpx>=0.24.0", "python-multipart>=0.0.6", "toml>=0.10.0",
        "distro>=1.7.0", "jiter>=0.4.0", "astrapy>=0.7.0",
        "markdown>=3.4.0", "apify-client>=1.0.0"
    ]
    
    for package in core_packages:
        try:
            print(f"Installing {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to install {package}: {e}")
            # Continue anyway - non-critical failures shouldn't stop everything

def install_langchain_dependencies():
    """Install LangChain dependencies"""
    print("Installing LangChain dependencies...")
    
    langchain_packages = [
        "langchain>=0.1.0", "langchain-core>=0.1.0", "langchain-openai>=0.0.3",
        "openai>=1.10.0", "langchain-anthropic>=0.1.0", "langchain-cohere>=0.1.0",
        "langchain-google-genai>=0.0.8", "langchain-google-community>=0.0.6",
        "langchain-community>=0.0.25", "langchain-chroma>=0.0.1"
    ]
    
    for package in langchain_packages:
        try:
            print(f"Installing {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to install {package}: {e}")

def install_additional_dependencies():
    """Install additional tool dependencies"""
    print("Installing additional dependencies...")
    
    additional_packages = [
        "crewai>=0.20.0", "crewai_tools>=0.1.0", "tavily-python>=0.2.8",
        "sentence-transformers>=2.2.0", "faiss-cpu>=1.7.0", "pypdf>=3.0.0",
        "unstructured>=0.10.0", "tiktoken>=0.5.0", "chromadb>=0.4.0",
        "beautifulsoup4>=4.10.0", "selenium>=4.10.0", "requests>=2.28.0",
        "gitpython>=3.1.30", "tqdm>=4.64.0", "pillow>=10.0.0"
    ]
    
    for package in additional_packages:
        try:
            print(f"Installing {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to install {package}: {e}")
            
def install_langflow():
    """Install langflow from local directory"""
    print("Installing Langflow package...")
    
    # Install langflow package from the backend/base directory
    backend_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "backend", "base")
    print(f"Installing langflow from {backend_base_path}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", backend_base_path])
        print("Successfully installed Langflow package")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Langflow package: {e}")
        return False
    
    return True

def install_dependencies():
    """Install all dependencies"""
    start_time = time.time()
    
    install_core_dependencies()
    install_langchain_dependencies()
    install_additional_dependencies()
    success = install_langflow()
    
    end_time = time.time()
    print(f"Total installation time: {end_time - start_time:.2f} seconds")
    return success

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

# Deploying Langflow on Replit

This document provides instructions for deploying this Langflow fork on Replit with the focused dependencies approach.

## Overview

This deployment uses a streamlined approach with only the necessary dependencies for the key functionalities:
- Google services integration
- CrewAI nodes/services
- RAG simplification nodes
- ChromaDB node dependencies
- Firecrawl dependencies
- Monkey Agent functionality

## Setup Instructions

1. **Fork this repository to Replit**
   - Go to Replit.com
   - Click "Create Repl" 
   - Select "Import from GitHub"
   - Enter your repository URL: `https://github.com/jononovo/langflow-master-v1.git`
   - Select the branch: `windsurf_250505` (or your current branch)

2. **Replit Setup Files**
   - The repository includes:
     - `.replit` - Basic configuration for Replit
     - `replit.nix` - System dependencies for the build
     - `replit_start.py` - Custom startup script
     - `requirements-focused.txt` - Focused Python dependencies

3. **Configuration**
   - If using OpenAI or other services, set your API keys as Replit Secrets:
     - Go to "Secrets" in the tools panel
     - Add secrets (e.g., `OPENAI_API_KEY`, etc.)

4. **Deployment Process**
   - Replit will automatically run `replit_start.py` when you click "Run"
   - This script:
     - Installs the langflow package from the local backend base directory
     - Installs the focused dependencies from `requirements-focused.txt`
     - Starts the Langflow server with proper static file configuration
   - The process might take 5-10 minutes for the initial setup

## Testing Your Deployment

Once deployed, test the Monkey Agent functionality with these commands:

1. Individual Nodes:
   - `add text input`
   - `add chat input`
   - `add openai embeddings`
   - `add openai`

2. Connections:
   - `add text input and connect to openai`
   - `connect text input to openai`
   - `add chat input and connect to openai embeddings`

3. API Testing:
   - Check `/api/v1/monkey-agent/test` endpoint to verify the backend API

## Troubleshooting

If you encounter issues:

1. **Dependency errors**:
   - Check the logs for any missing packages
   - Add them to `requirements-focused.txt` if needed

2. **Frontend not loading**:
   - Verify the frontend build directory exists at `src/frontend/build`
   - If missing, run the build process or use a pre-built version

3. **Port issues**:
   - Replit automatically handles port forwarding
   - The application runs on port 8080 internally
   
4. **API errors**:
   - Check logs for import or module errors
   - Verify the Monkey Agent module path is correct in your Langflow installation

## Additional Notes

- The focused installation significantly reduces build time and resource usage
- Any changes to dependencies should be made in `requirements-focused.txt`
- For development, you may want to refer to the full requirements in the original Langflow repository

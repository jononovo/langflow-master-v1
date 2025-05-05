FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    build-essential \
    gcc \
    g++ \
    git \
    curl \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire repository
COPY . .

# Install backend dependencies
RUN echo "Installing backend requirements" && \
    if [ -f "src/backend/requirements.txt" ]; then \
        pip install -r src/backend/requirements.txt; \
    elif [ -f "src/backend/base/requirements.txt" ]; then \
        pip install -r src/backend/base/requirements.txt; \
    elif [ -f "requirements.txt" ]; then \
        pip install -r requirements.txt; \
    else \
        echo "No requirements.txt found in expected locations"; \
        find . -name "requirements.txt" -type f; \
        exit 1; \
    fi

# Add backend to Python path
ENV PYTHONPATH=/app/src/backend:${PYTHONPATH}

# Install frontend dependencies and build
RUN cd src/frontend && npm install && npm run build

# Set environment variables
ENV PORT=8080
ENV HOST=0.0.0.0

# Expose the port
EXPOSE 8080

# Start the application
CMD ["sh", "-c", "cd src/backend && python -m langflow run --host 0.0.0.0 --port 8080"]

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

# Install backend dependencies with verbose output
RUN cd src/backend && pip install --verbose -e . || { echo "Backend installation failed"; exit 1; }

# Install frontend dependencies and build
RUN cd src/frontend && npm install && npm run build

# Set environment variables
ENV PORT=8080
ENV HOST=0.0.0.0

# Expose the port
EXPOSE 8080

# Start the application
CMD ["sh", "-c", "cd src/backend && python -m langflow run --host 0.0.0.0 --port 8080"]

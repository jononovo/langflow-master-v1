FROM python:3.10-slim

WORKDIR /app

# Install Node.js
RUN apt-get update && apt-get install -y nodejs npm

# Copy the entire repository
COPY . .

# Install backend dependencies
RUN cd src/backend && pip install -e .

# Install frontend dependencies and build
RUN cd src/frontend && npm install && npm run build

# Set environment variables
ENV PORT=8080
ENV HOST=0.0.0.0

# Expose the port
EXPOSE 8080

# Start the application
CMD ["sh", "-c", "cd src/backend && python -m langflow run --host 0.0.0.0 --port 8080"]

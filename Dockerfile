# Use a smaller base image to keep final image lightweight
FROM python:3.11-slim

# Set environment variables early (before installing anything)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Create working directory
WORKDIR /app    

# Pre-install system dependencies (like gcc, libpq if needed)
# RUN apt-get update && apt-get install -y build-essential

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Use non-root user (optional for security)
# RUN useradd -m appuser && chown -R appuser /app
# USER appuser

# Set default command to start FastAPI server
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000","--reload"]

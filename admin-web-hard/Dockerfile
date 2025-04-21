FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for Docker caching efficiency)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY app.py .
COPY static/ static/

# Create dummy logs file
RUN echo -e "Sample log line 1\nSample log line 2" > /app/logs.txt

# Expose Flask default port (optional)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

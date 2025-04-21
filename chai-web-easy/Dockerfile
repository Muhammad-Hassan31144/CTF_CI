FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app (including static, templates if any)
COPY . .

# Optional: Expose port (Flask default)
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "app.py"]

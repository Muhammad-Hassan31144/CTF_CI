FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first (use Docker cache effectively)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app (including static or templates if added later)
COPY . .

# Optional: Document Flask default port (doesn't publish, just for info)
EXPOSE 5000

# Set environment to production-safe Flask mode
ENV FLASK_ENV=production

# Run the Flask app directly
CMD ["python", "app.py"]

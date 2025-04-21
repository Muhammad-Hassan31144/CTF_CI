# Use lightweight Python base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app and dataset into container
COPY reversal_recall.py .
COPY reversal_recall.csv .

# Install dependencies
RUN pip install flask pandas

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "reversal_recall.py"]

FROM python:3.9-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies with specific versions
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "-u", "server.py"]
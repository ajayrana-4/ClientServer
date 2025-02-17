FROM python:3.9-slim

# Use a mirror for Debian repository
RUN touch /etc/apt/sources.list && sed -i 's/deb.debian.org/mirrors.kernel.org/g' /etc/apt/sources.list \
    && apt-get update && apt-get install -y \
    dnsutils \
    net-tools \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .


# Run the application
CMD ["python", "-u", "client.py"]
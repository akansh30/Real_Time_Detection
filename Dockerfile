FROM python:3.13-alpine

# Set working directory inside the container
WORKDIR /app

# Install basic system dependencies for OpenCV
RUN apk add --no-cache \
    ffmpeg \
    libsm \
    libxext \
    libgl1 \
    && rm -rf /var/cache/apk/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose if needed
EXPOSE 5000

# Run your app
CMD ["python", "main.py"]

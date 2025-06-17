# Python base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY ./requirements.txt /app/requirements.txt


# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose port 8090
EXPOSE 8090

# Command to run the application
CMD ["python", "main.py"]

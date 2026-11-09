# Use Python as the base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency list into the container


# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container


# Document the port used by Flask


# Start the Flask application

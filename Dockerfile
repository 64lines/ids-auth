# Use an official Python runtime as a parent image
FROM python:3.10.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Set the environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port that Flask is listening on
EXPOSE 5000

# Run the Flask application
CMD ["/bin/bash", "-c", "source venv/bin/activate && flask run --host=0.0.0.0"]

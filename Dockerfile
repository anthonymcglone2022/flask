# Use the official Python image as a base
FROM python:3.9-slim

# Install Flask
RUN pip install flask

# Expose ports for Flask
EXPOSE 5000

WORKDIR /workspace
COPY . /workspace

ENTRYPOINT ["python", "app.py"]
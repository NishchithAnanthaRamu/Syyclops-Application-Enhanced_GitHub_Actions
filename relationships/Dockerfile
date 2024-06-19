# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install IfcOpenShell and other necessary dependencies
RUN apt-get update && apt-get install -y \
    libboost-all-dev \
    cmake \
    build-essential \
    python3-dev \
    libpython3-dev \
    libxml2-dev \
    libgeos-dev \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*
	

# Decompress the packages
RUN tar -xJvf ifcopenshell.tar.xz

# Install Python dependencies
RUN pip install --upgrade pip

# copy ifcopenshell dir to python path - site packages
RUN cp -r /app/ifcopenshell /usr/local/lib/python3.9/site-packages/.

# install lark dependency
RUN pip install lark-parser

# Define environment variable
ENV NAME IfcOpenShellApp

# Run the application
CMD ["python3", "relationships.py"]


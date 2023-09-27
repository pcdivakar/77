# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local requirements file to the container at /usr/src/app
COPY requirements.txt ./

# Set up the index URL for pip
RUN pip config set global.index-url https://pypi.python.org/simple/

# Install any needed packages specified in requirements.txt
RUN pip install --default-timeout=100 -r requirements.txt

# Upgrade pip
RUN pip install --upgrade pip

# Copy the local directory to the container at /usr/src/app
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

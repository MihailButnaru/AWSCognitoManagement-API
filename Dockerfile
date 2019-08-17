# Official Python runtime as a parent image
from python:3-slim

# Copy the requiremts txt and the gunicorn config file
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn gevent aiohttp
COPY gunicorn.cfg /gunicorn.cfg

# Copy the current directory contents into the container at /api/aws-api
COPY  . /api/aws-api 

# Set the working directory to /api/aws-api
WORKDIR /api/aws-api
ADD setup.py .
ADD LICENSE . 
ADD README.md .
ADD requirements.txt . 

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the gunicorn config for the production
CMD ["gunicorn", "--config", "/gunicorn.cfg", "-b", "0.0.0.0:5000", "api:app"]

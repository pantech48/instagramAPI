# Start from a base Python 3.9 image
FROM python:3.9-slim-buster

# Set a directory for our application
WORKDIR /usr/src/app

# Copy over our requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# Install pip requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy over the rest of our application
COPY . /usr/src/app

# Expose port 8080 for our application
EXPOSE 8080

# The command to run our application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

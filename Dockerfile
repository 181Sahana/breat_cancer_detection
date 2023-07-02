# Use the official Python base image
FROM python:3.9

# Set the working directory inside the Docker image
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that your FastAPI application will listen on
EXPOSE 8080

# Specify the command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

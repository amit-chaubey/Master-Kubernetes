FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files and install dependencies
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

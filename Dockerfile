# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the wait-for-mysql script into the container
COPY wait-for-mysql.sh .

# Make the script executable
RUN chmod +x wait-for-mysql.sh

# Copy the current directory contents into the container
COPY . .

# Expose port 8000 for the app
EXPOSE 8000

# Run the Django development server using the wait-for-mysql script
CMD ["./wait-for-mysql.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]

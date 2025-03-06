FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Install
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available
EXPOSE 80

# Define environment variable
ENV NAME ChessBot

# Run the application
CMD ["python", "app.py"]

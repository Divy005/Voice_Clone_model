# Start with a standard Python 3.11 image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the specific PyTorch version first for compatibility
RUN pip install --no-cache-dir torch==2.3.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121

# Install the rest of the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code (main.py) into the container
COPY main.py .

# Expose the port the app will run on. Hosting services like Hugging Face
# and AWS App Runner often expect port 8080.
EXPOSE 8080

# The command to run your application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

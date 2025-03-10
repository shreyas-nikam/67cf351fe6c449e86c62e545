# Use Python base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Update system and install additional necessary packages
RUN apt-get update && apt-get install -y build-essential

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set the internal port for Streamlit
ENV PORT=8501

# Expose the port so Docker maps it
EXPOSE $PORT

# Run Streamlit in headless mode
CMD ["bash", "-c", "streamlit run app.py --server.port=$PORT --server.headless=true"]

# Use Python base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies and additional libraries for plotting support
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get update && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

# Copy the rest of the application code
COPY . /app

# Set the port number via build-time or run-time environment; DO NOT change this port.
ENV PORT=8501

# Expose the port
EXPOSE $PORT

# Run Streamlit
CMD ["bash", "-c", "streamlit run app.py --server.port=$PORT --server.headless=true"]

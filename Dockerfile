
# Use Python base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code
COPY . /app

# Set the port number via environment variable (default 8501)
ENV PORT=8501

# Expose the port for Streamlit
EXPOSE $PORT

# Run Streamlit in headless mode
CMD ["bash", "-c", "streamlit run app.py --server.port=$PORT --server.headless=true"]

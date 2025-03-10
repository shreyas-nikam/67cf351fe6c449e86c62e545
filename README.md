# Trigonometric Functions of Any Angle Exploration

This Streamlit application provides an interactive exploration of trigonometric functions for any angle. The app is organized as a multipage application, each focusing on different functionalities such as angle input, unit circle visualization, and interactive charts.

## Features

- **Angle Input and Computation:** Input an angle (in degrees or radians) and view computed trigonometric values (sine, cosine, tangent, cosecant, secant, cotangent).
- **Unit Circle Visualization:** Visualize the unit circle with the input angle marked.
- **Interactive Charts:** Dynamic charts display how trigonometric functions change over a full cycle.

## How to Run

### Locally
1. Install required libraries:
   ```
   pip install -r requirements.txt
   ```
2. Run the application:
   ```
   streamlit run app.py
   ```

### Using Docker
1. Build the Docker image:
   ```
   docker build -t trig_app .
   ```
2. Start the container using docker-compose:
   ```
   docker-compose up
   ```

## Folder Structure

- `app.py`: Main entry point.
- `pages/`: Contains additional pages for the multipage app.
- `Dockerfile`: Docker image definition.
- `docker-compose.yml`: Docker Compose configuration.
- `requirements.txt`: Python dependencies.

## Explanation

This interactive app is designed to help users explore and understand trigonometric functions using dynamic visualizations and real-time interactivity.

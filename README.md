# Trigonometric Functions of Any Angle Exploration

This Streamlit application helps users explore trigonometric functions for any angle. It is designed to support learning through interactive visualizations and computations of sine, cosine, tangent, cosecant, secant, and cotangent functions.

## Features
- Enter an angle using a text box or slider.
- Switch between degrees and radians.
- Visualize the angle on a dynamically plotted unit circle.
- Compute and display all primary trigonometric function values.
- Interactive charts showing trends in trigonometric functions.

## How to Run
1. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
2. Run the application with:
   ```
   streamlit run app.py
   ```

## Docker Usage
This repository includes a Dockerfile and a docker-compose.yml file. To run using Docker:
1. Build the Docker image:
   ```
   docker-compose build
   ```
2. Run the container:
   ```
   docker-compose up
   ```
The app will run on the internal port 8501.

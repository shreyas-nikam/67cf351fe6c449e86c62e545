
# Codelab: Trigonometric Functions of Any Angle Exploration

## Introduction
This technical codelab explains the development of the **Trigonometric Functions Lab**, a multipage Streamlit application. The purpose of the lab is to provide an interactive exploration of trigonometric functions for any angle.

## Application Structure

### 1. app.py
- **Multipage Navigation:**  
  Uses `st.sidebar.selectbox` to allow users to switch between pages:
  - **Unit Circle:** Visualizes a unit circle with an indicated angle and computes (x, y) coordinates.
  - **Trigonometric Functions:** Displays computed values for sine, cosine, tangent, cosecant, secant, and cotangent.
  - **Interactive Charts:** Provides dynamic charts (using matplotlib) that show how trigonometric function values change as the angle varies.
  - **About:** Offers a comprehensive explanation of the application and theoretical background.
  
- **Angle Input:**  
  Users set the angle using a number input widget and choose between degrees or radians via a radio button.
  
- **Visualization:**  
  The unit circle is plotted using matplotlib. The computed point (x, y) is distinctly marked, and a dashed line indicates the radius corresponding to the input angle.
  
- **Computation:**  
  Trigonometric values are calculated using Python’s `math` module, with error handling for undefined functions (e.g., when cosine is zero).

### 2. README.md
Provides an overview of the lab, usage instructions, and technical specifications for both developers and users.

### 3. requirements.txt
Contains all the dependencies required by the application:

### 4. Dockerfile and docker-compose.yml
- **Dockerfile:**  
  Based on the `python:3.12-slim` image, it prepares the environment, installs dependencies, and runs Streamlit on the specified port (8501).
  
- **docker-compose.yml:**  
  Configures the container service, ensuring the application is available through the correct external port mapping (`8504:8501`) and maintains the provided lab id.

## Detailed Code Explanation
- **Multipage App Development:**  
  The structure of the multipage app allows easy maintenance and modular development of functionalities. Each section (unit circle, trig functions, charts, and about) is separated for clarity.
  
- **Interactive Elements:**  
  The application extensively uses Streamlit widgets like sliders, radio buttons, and number inputs to create an interactive user experience.
  
- **Visualization Techniques:**  
  matplotlib is used to create dynamic visualizations. The unit circle plot illustrates the basic concepts of trigonometry geometrically while interactive charts demonstrate real-time changes in function values.
  
- **Educational Integration:**  
  Inline help, clear annotations, and tooltips have been added throughout the app to provide context and explanations for each functionality, thereby reinforcing the theoretical foundations introduced in Section 4.3 of the accompanying document.

## Conclusion
This lab combines Streamlit’s interactive framework with powerful Python libraries to create an engaging educational tool. It not only demonstrates the computation of trigonometric functions but also visually explains these mathematical concepts through dynamic plots and detailed documentation.

# Trigonometric Functions Exploration Lab

## Description

Welcome to the **Trigonometric Functions Exploration Lab**, an interactive Streamlit application designed to deepen your understanding of trigonometric functions for any angle. This application goes beyond the basics of acute angles (0-90 degrees) and allows you to explore the behavior of sine, cosine, tangent, and their reciprocal functions across the full spectrum of angles.

**Key Features:**

- **Interactive Angle Input:** Choose between Degrees and Radians to input your angle and instantly observe the results.
- **Dynamic Unit Circle Visualization:** See your chosen angle represented on a unit circle, providing a clear geometric interpretation of trigonometric functions.
- **Real-time Function Values:** Watch as the values of sine, cosine, tangent, cosecant, secant, and cotangent dynamically update as you adjust the angle.
- **Interactive Charts:** Explore the trends and periodic nature of sine, cosine, and tangent functions through interactive visualizations that respond to angle changes.
- **Educational and Self-Contained:** This application is designed for educational purposes and operates using synthetic data, ensuring a smooth and focused learning experience without external dependencies.

This lab is perfect for students, educators, or anyone looking to visualize and understand trigonometric functions in a dynamic and intuitive way.

## Installation

To run this Streamlit application, you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org).

Once Python is installed, follow these steps to install the necessary libraries and run the application:

1. **Clone the repository (if applicable):**
   If you have access to the application code repository, clone it to your local machine using Git:
   ```bash
   git clone [repository_url]
   cd [repository_directory]
   ```
   If you have the code as a Python file (e.g., `app.py`), place it in a directory on your local machine.

2. **Install required Python libraries:**
   Open your terminal or command prompt, navigate to the application directory, and install the required libraries using pip:
   ```bash
   pip install streamlit numpy matplotlib
   ```
   This command will install Streamlit, NumPy, and Matplotlib, which are necessary for running the application.

## Usage

1. **Run the Streamlit application:**
   In your terminal or command prompt, navigate to the directory containing the application file (e.g., `app.py`) and run the following command:
   ```bash
   streamlit run app.py
   ```
   Replace `app.py` with the actual name of your Python file if it's different.

2. **Access the application in your browser:**
   Streamlit will automatically launch the application in your default web browser. If it doesn't open automatically, you can usually access it by navigating to the URL displayed in your terminal (typically `http://localhost:8501`).

3. **Interact with the application:**
   Once the application is running in your browser, you can interact with the following elements:

   - **Sidebar Settings:**
     - **Input Mode:** Choose between "Degrees" and "Radians" to specify the angle unit.
     - **Enter Angle:** Use the number input field to type in a specific angle value.
     - **Adjust Angle Interactively:** Use the slider to dynamically change the angle and observe real-time updates in the unit circle, function values, and charts.

   - **Unit Circle Visualization:**
     - Observe the unit circle on the left side of the main panel. The red line represents the angle you've inputted, and the red dot shows where this angle intersects the unit circle. The coordinates of this point are also displayed.

   - **Trigonometric Function Values:**
     - On the right side of the main panel, you'll see the calculated values for sine, cosine, tangent, cosecant, secant, and cotangent for the entered angle. "Undefined" will be displayed for functions that are undefined at the given angle.

   - **Interactive Charts (Function Trends):**
     - Scroll down to see interactive charts displaying the trends of sine, cosine, and tangent functions as the angle varies from -360° to 360°. These charts dynamically update as you change the angle using the slider in the sidebar.

   Experiment with different angle inputs and observe how the unit circle, function values, and charts change in real-time to enhance your understanding of trigonometric functions.

## Credits

Developed by QuantUniversity.

- [QuantUniversity Website](https://www.quantuniversity.com)

## License

© 2025 QuantUniversity. All Rights Reserved.

This application is provided for educational purposes. For inquiries regarding commercial use or redistribution, please contact QuantUniversity. Any reproduction of this demonstration requires prior written consent from QuantUniversity.

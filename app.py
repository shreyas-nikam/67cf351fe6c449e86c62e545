import streamlit as st
import numpy as np
import math
import matplotlib.pyplot as plt

st.title("Trigonometric Functions of Any Angle Exploration")

# Sidebar settings for input method and units
input_method = st.sidebar.selectbox("Select input method", options=["Input box", "Slider"])
unit_mode = st.sidebar.radio("Select angle unit", options=["Degrees", "Radians"])

if input_method == "Input box":
    angle_input = st.sidebar.text_input("Enter angle:", "0")
    try:
        angle = float(angle_input)
    except:
        st.error("Please enter a valid number.")
        angle = 0.0
else:
    angle = st.sidebar.slider("Select angle", min_value=-360.0, max_value=360.0, value=0.0)

# Convert angle to radians if input is in degrees
angle_rad = math.radians(angle) if unit_mode == "Degrees" else angle

# Compute trigonometric functions
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)
cosec_val = 1/sin_val if sin_val != 0 else float('inf')
sec_val = 1/cos_val if cos_val != 0 else float('inf')
cot_val = 1/tan_val if tan_val != 0 else float('inf')

# Display computed function values
st.subheader("Trigonometric Function Values")
st.write(f"Angle: {angle} {unit_mode} (in radians: {angle_rad:.4f})")
st.write(f"Sine: {sin_val:.4f}")
st.write(f"Cosine: {cos_val:.4f}")
st.write(f"Tangent: {tan_val:.4f}")
st.write(f"Cosecant: {cosec_val:.4f}")
st.write(f"Secant: {sec_val:.4f}")
st.write(f"Cotangent: {cot_val:.4f}")

# Plot the unit circle and the angle line
theta = np.linspace(0, 2 * np.pi, 300)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x_circle, y_circle, label="Unit Circle")
ax.plot([0, math.cos(angle_rad)], [0, math.sin(angle_rad)], 'r-', label="Angle")
ax.scatter([math.cos(angle_rad)], [math.sin(angle_rad)], color='red', zorder=5)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Unit Circle with Angle')
ax.legend()

st.pyplot(fig)

# Additional interactive line chart for sine function over a full period
angles = np.linspace(0, 2*np.pi, 100)
sine_values = np.sin(angles)
chart_data = {"Angle (radians)": angles, "Sine": sine_values}
st.line_chart(chart_data)

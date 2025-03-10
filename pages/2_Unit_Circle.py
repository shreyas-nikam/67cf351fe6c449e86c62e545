import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Unit Circle Visualization", layout="wide")

st.title("Unit Circle Visualization")
st.markdown("""
This page displays the unit circle and shows the intersection point corresponding to your input angle.
""")

input_mode = st.radio("Select Input Mode", ["Degrees", "Radians"], key="unit_circle_mode")
angle_input = st.number_input("Enter the angle value", value=0.0, key="unit_circle_angle")
if input_mode == "Degrees":
    angle_rad = math.radians(angle_input)
else:
    angle_rad = angle_input

# Generate the unit circle data
theta = np.linspace(0, 2*np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# Compute the point on the circle
x_point = math.cos(angle_rad)
y_point = math.sin(angle_rad)

fig, ax = plt.subplots()
ax.plot(x_circle, y_circle, label="Unit Circle")
ax.plot([0, x_point], [0, y_point], "r-", label="Radius to Angle")
ax.plot(x_point, y_point, "bo", label=f"({x_point:.2f}, {y_point:.2f})")
ax.set_aspect("equal", adjustable="box")
ax.set_title("Unit Circle")
ax.legend()
st.pyplot(fig)

st.markdown("#### Explanation")
st.write(
    "The unit circle is plotted using matplotlib. Your input angle (converted to radians if necessary) "
    "determines a point on the circle. A line is drawn from the origin to this point to illustrate the angle."
)

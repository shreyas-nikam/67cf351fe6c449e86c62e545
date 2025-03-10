import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Interactive Charts", layout="wide")
st.title("Interactive Charts for Trigonometric Functions")
st.markdown("""
Adjust the angle using the slider below to see how the trigonometric function values change over a full cycle.
""")

angle_deg = st.slider("Select Angle (in degrees)", 0, 360, 0)
angle_rad = math.radians(angle_deg)

# Create a range of angles from 0 to 2π
angles = np.linspace(0, 2*np.pi, 360)
sin_vals = np.sin(angles)
cos_vals = np.cos(angles)
tan_vals = np.tan(angles)
# Limit extreme tangent values for visualization
tan_vals = np.where(np.abs(tan_vals) > 10, np.nan, tan_vals)

fig, ax = plt.subplots(1, 3, figsize=(18, 5))
# Sine function
ax[0].plot(np.degrees(angles), sin_vals, label="Sine")
ax[0].set_title("Sine Function")
ax[0].set_xlabel("Angle (degrees)")
ax[0].set_ylabel("Value")
ax[0].axvline(angle_deg, color="red", linestyle="--", label=f"Angle = {angle_deg}°")
ax[0].legend()

# Cosine function
ax[1].plot(np.degrees(angles), cos_vals, color="green", label="Cosine")
ax[1].set_title("Cosine Function")
ax[1].set_xlabel("Angle (degrees)")
ax[1].set_ylabel("Value")
ax[1].axvline(angle_deg, color="red", linestyle="--", label=f"Angle = {angle_deg}°")
ax[1].legend()

# Tangent function
ax[2].plot(np.degrees(angles), tan_vals, color="purple", label="Tangent")
ax[2].set_title("Tangent Function")
ax[2].set_xlabel("Angle (degrees)")
ax[2].set_ylabel("Value")
ax[2].axvline(angle_deg, color="red", linestyle="--", label=f"Angle = {angle_deg}°")
ax[2].legend()

st.pyplot(fig)

st.markdown("#### Explanation")
st.write(
    "The above charts demonstrate how the sine, cosine, and tangent functions vary over a complete cycle (0° to 360°). "
    "The red dashed line indicates the selected angle. Extreme values in the tangent function are omitted from the plot for clarity."
)

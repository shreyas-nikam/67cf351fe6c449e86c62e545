import streamlit as st
import math

st.set_page_config(page_title="Angle Input & Computation", layout="wide")

st.title("Angle Input and Computation")
st.markdown("""
This page allows you to input an angle and see the computed values of various trigonometric functions.

- **Degrees or Radians:** Choose your input mode.
- **Input:** Provide the angle value.
""")

input_mode = st.radio("Select Input Mode", ["Degrees", "Radians"])
angle_input = st.number_input("Enter the angle value", value=0.0)

if input_mode == "Degrees":
    angle_rad = math.radians(angle_input)
else:
    angle_rad = angle_input

# Compute trigonometric functions
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad) if math.cos(angle_rad) != 0 else float('inf')
cosec_val = 1/sin_val if sin_val != 0 else float('inf')
sec_val = 1/cos_val if cos_val != 0 else float('inf')
cot_val = 1/tan_val if tan_val != 0 else float('inf')

st.markdown("### Computed Trigonometric Values")
st.write(f"Sine: {sin_val}")
st.write(f"Cosine: {cos_val}")
st.write(f"Tangent: {tan_val}")
st.write(f"Cosecant: {cosec_val}")
st.write(f"Secant: {sec_val}")
st.write(f"Cotangent: {cot_val}")

st.markdown("#### Explanation")
st.write(
    "The above values are computed using the standard Python math library. "
    "If the input is in degrees, it is converted to radians before computation."
)

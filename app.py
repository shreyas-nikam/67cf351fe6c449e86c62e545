import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Trigonometric Functions Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Trigonometric Functions of Any Angle Exploration")
st.divider()

# Explanation of the Application
st.write(
    """
    **Welcome to the Trigonometric Functions Exploration Lab!**

    This interactive application is designed to enhance your understanding of trigonometric functions for any angle, 
    extending beyond acute angles (0-90 degrees). 
    Explore how sine, cosine, tangent, and their reciprocals behave across the entire range of angles.

    **Key Features:**
    - **Interactive Angle Input:** Enter angles in degrees or radians and instantly see the results.
    - **Dynamic Unit Circle:** Visualize your angle on a unit circle, understanding the geometric interpretation of trigonometric functions.
    - **Real-time Function Values:** Observe how trigonometric function values change as you adjust the angle.
    - **Interactive Charts:** Explore trends and relationships between different trigonometric functions through dynamic visualizations.

    This lab is self-contained and uses synthetic data for demonstration purposes, ensuring a seamless educational experience.
    """
)

st.subheader("Angle Input and Unit Circle Visualization")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    angle_input_mode = st.radio("Input Mode", ["Degrees", "Radians"], index=0)
    angle_value = st.number_input(
        "Enter Angle", value=0.0, format="%.2f"
    )
    angle_slider = st.slider("Adjust Angle Interactively", -360, 360, 0, step=1)
    angle_value = float(angle_slider) if angle_input_mode == "Degrees" else float(angle_slider * math.pi / 180)
    st.caption("Use the slider or number input to change the angle and observe real-time updates.")


if angle_input_mode == "Degrees":
    angle_radians = math.radians(angle_value)
    angle_degrees_display = angle_value
    angle_radians_display = angle_radians
else:
    angle_radians = angle_value
    angle_degrees_display = math.degrees(angle_value)
    angle_radians_display = angle_value

col1, col2 = st.columns(2)

with col1:
    st.subheader("Unit Circle")
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), 1, facecolor='none', edgecolor='blue')
    ax.add_patch(circle)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_title('Unit Circle with Angle')

    # Plotting the angle
    x = math.cos(angle_radians)
    y = math.sin(angle_radians)
    ax.plot([0, x], [0, y], 'r-', linewidth=2)
    ax.plot(x, y, 'ro', markersize=8) # Point on the circle
    ax.text(x*1.1, y*1.1, f'({x:.2f}, {y:.2f})', verticalalignment='bottom', horizontalalignment='left')

    # Annotate the angle value
    angle_degrees_text = f"{angle_degrees_display:.2f}°" if angle_input_mode == "Degrees" else f"{angle_radians_display:.2f} radians"
    ax.text(0.1, 0.1, angle_degrees_text, fontsize=10, color='green')


    st.pyplot(fig)
    st.caption("Visualization of the angle on the Unit Circle. The red line represents the angle, and the red dot indicates where the angle intersects the unit circle.")


with col2:
    st.subheader("Trigonometric Function Values")
    sin_val = math.sin(angle_radians)
    cos_val = math.cos(angle_radians)
    tan_val = math.tan(angle_radians)
    csc_val = 1/sin_val if sin_val != 0 else float('inf')
    sec_val = 1/cos_val if cos_val != 0 else float('inf')
    cot_val = 1/tan_val if tan_val != 0 and tan_val != float('inf') else float('inf') if tan_val == 0 else 0 # cot is 0 when tan is inf, inf when tan is 0

    st.write(f"**Angle ({angle_input_mode.lower()}):** {angle_degrees_display:.2f}°" if angle_input_mode == "Degrees" else f"**Angle ({angle_input_mode.lower()}):** {angle_radians_display:.2f} radians")
    st.write(f"**sin(θ):** {sin_val:.4f}")
    st.write(f"**cos(θ):** {cos_val:.4f}")
    st.write(f"**tan(θ):** {tan_val:.4f}" if tan_val != float('inf') else "**tan(θ):** Undefined")
    st.write(f"**csc(θ):** {csc_val:.4f}" if csc_val != float('inf') else "**csc(θ):** Undefined")
    st.write(f"**sec(θ):** {sec_val:.4f}" if sec_val != float('inf') else "**sec(θ):** Undefined")
    st.write(f"**cot(θ):** {cot_val:.4f}" if cot_val != float('inf') else "**cot(θ):** Undefined")
    st.caption("These are the calculated values for the six trigonometric functions based on the input angle.")


st.divider()
st.subheader("Interactive Charts: Function Trends")
st.write("Observe how trigonometric functions vary with changing angles. Use the slider in the sidebar to adjust the angle and see the dynamic updates in the charts below.")

angle_range_degrees = np.arange(-360, 361, 1)
angle_range_radians = np.radians(angle_range_degrees)
sin_values = np.sin(angle_range_radians)
cos_values = np.cos(angle_range_radians)
tan_values = np.tan(angle_range_radians)


chart_col1, chart_col2, chart_col3 = st.columns(3)

with chart_col1:
    st.caption("Sine Function Trend")
    fig_sin_chart, ax_sin_chart = plt.subplots()
    ax_sin_chart.plot(angle_range_degrees, sin_values, label='sin(θ)', color='red')
    ax_sin_chart.set_xlabel("Angle (Degrees)")
    ax_sin_chart.set_ylabel("sin(θ)")
    ax_sin_chart.set_title("Sine Function vs Angle")
    ax_sin_chart.legend()
    st.pyplot(fig_sin_chart)
    st.caption("This line chart displays how the sine function value changes as the angle varies from -360° to 360°. Notice the periodic nature of the sine function.")


with chart_col2:
    st.caption("Cosine Function Trend")
    fig_cos_chart, ax_cos_chart = plt.subplots()
    ax_cos_chart.plot(angle_range_degrees, cos_values, label='cos(θ)', color='green')
    ax_cos_chart.set_xlabel("Angle (Degrees)")
    ax_cos_chart.set_ylabel("cos(θ)")
    ax_cos_chart.set_title("Cosine Function vs Angle")
    ax_cos_chart.legend()
    st.pyplot(fig_cos_chart)
    st.caption("This line chart displays how the cosine function value changes with the angle. Like sine, cosine is also periodic but shifted.")


with chart_col3:
    st.caption("Tangent Function Trend")
    fig_tan_chart, ax_tan_chart = plt.subplots()
    ax_tan_chart.plot(angle_range_degrees, tan_values, label='tan(θ)', color='purple')
    ax_tan_chart.set_xlabel("Angle (Degrees)")
    ax_tan_chart.set_ylabel("tan(θ)")
    ax_tan_chart.set_title("Tangent Function vs Angle")
    ax_tan_chart.legend()
    st.pyplot(fig_tan_chart)
    st.caption("This line chart shows the tangent function's behavior across angles. Observe the asymptotes and the periodicity, which is different from sine and cosine.")


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")

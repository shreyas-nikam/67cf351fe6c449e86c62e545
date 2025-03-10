
import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Function to plot unit circle and mark the given angle
def plot_unit_circle(angle, angle_unit):
    # Convert angle to radians if needed
    if angle_unit == "Degrees":
        angle_rad = math.radians(angle)
    else:
        angle_rad = angle
    
    # Calculate x, y coordinates on the circle
    x = math.cos(angle_rad)
    y = math.sin(angle_rad)
    
    fig, ax = plt.subplots(figsize=(5,5))
    circle = plt.Circle((0, 0), 1, color='lightblue', fill=False, linewidth=2)
    ax.add_artist(circle)
    # Plot x and y axes
    ax.axhline(0, color='grey', lw=1)
    ax.axvline(0, color='grey', lw=1)
    # Plot the point on the circle
    ax.plot(x, y, 'ro', label=f'({x:.2f}, {y:.2f})')
    # Plot line from center to the point
    ax.plot([0, x], [0, y], 'r--')
    # Annotate the angle in degrees
    angle_display = angle if angle_unit == "Degrees" else math.degrees(angle)
    ax.text(0.1, 0.1, f'Angle: {angle_display:.2f}°', fontsize=12, color='purple')
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)
    ax.set_aspect('equal')
    ax.set_title("Unit Circle")
    ax.legend()
    return fig

# Function to calculate trigonometric functions
def trig_functions(angle, angle_unit):
    if angle_unit == "Degrees":
        angle_rad = math.radians(angle)
    else:
        angle_rad = angle

    # Compute trigonometric values
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    # Handle tangent where cosine is close to zero
    try:
        tangent = math.tan(angle_rad)
    except Exception:
        tangent = float('inf')
    
    # Compute reciprocal functions with proper exception handling
    cosecant = 1.0 / sine if abs(sine) > 1e-6 else float('inf')
    secant = 1.0 / cosine if abs(cosine) > 1e-6 else float('inf')
    cotangent = 1.0 / tangent if abs(tangent) > 1e-6 else float('inf')

    return {
        "Sine": sine,
        "Cosine": cosine,
        "Tangent": tangent,
        "Cosecant": cosecant,
        "Secant": secant,
        "Cotangent": cotangent
    }

# Multipage app navigation
st.sidebar.title("Trigonometric Functions Lab")
page = st.sidebar.selectbox("Navigation", ["Unit Circle", "Trigonometric Functions", "Interactive Charts", "About"])

# Common controls for angle input
st.sidebar.subheader("Angle Input Settings")
angle = st.sidebar.number_input("Enter an angle", value=45.0, step=1.0)
angle_unit = st.sidebar.radio("Select angle unit", ("Degrees", "Radians"))

if page == "Unit Circle":
    st.header("Unit Circle Visualization")
    st.write("This page displays a unit circle with an indicated angle and the corresponding (x, y) coordinates on the circle.")
    fig = plot_unit_circle(angle, angle_unit)
    st.pyplot(fig)
    st.write("The red dot indicates the point on the unit circle corresponding to the given angle.")
    
elif page == "Trigonometric Functions":
    st.header("Trigonometric Function Values")
    st.write("This page computes key trigonometric functions of the input angle and displays them.")
    results = trig_functions(angle, angle_unit)
    for key, value in results.items():
        st.write(f"**{key}**: {value:.4f}")
    st.write("The functions computed include sine, cosine, tangent and their reciprocals (cosecant, secant, and cotangent).")
    
elif page == "Interactive Charts":
    st.header("Interactive Charts")
    st.write("Adjust the slider to see how the trigonometric function values vary with changes in angle.")
    min_angle = st.slider("Select Minimum Angle", 0, 360, 0)
    max_angle = st.slider("Select Maximum Angle", 0, 360, 360)
    if min_angle >= max_angle:
        st.error("Minimum angle must be less than maximum angle.")
    else:
        angles = np.linspace(min_angle, max_angle, 100)
        if angle_unit == "Degrees":
            angles_rad = np.deg2rad(angles)
        else:
            angles_rad = angles
        sine_vals = np.sin(angles_rad)
        cosine_vals = np.cos(angles_rad)
        tangent_vals = np.tan(angles_rad)
        fig, ax = plt.subplots(1, 3, figsize=(18,5))
        ax[0].plot(angles, sine_vals, label="Sine", color="blue")
        ax[0].set_title("Sine vs Angle")
        ax[0].set_xlabel("Angle")
        ax[0].set_ylabel("Sine")
        ax[0].legend()
        ax[1].plot(angles, cosine_vals, label="Cosine", color="green")
        ax[1].set_title("Cosine vs Angle")
        ax[1].set_xlabel("Angle")
        ax[1].set_ylabel("Cosine")
        ax[1].legend()
        ax[2].plot(angles, tangent_vals, label="Tangent", color="red")
        ax[2].set_title("Tangent vs Angle")
        ax[2].set_xlabel("Angle")
        ax[2].set_ylabel("Tangent")
        ax[2].legend()
        st.pyplot(fig)
        st.write("These interactive charts illustrate how the trigonometric functions change as the angle varies.")
    
elif page == "About":
    st.header("About This Application")
    st.write("""
    **Trigonometric Functions of Any Angle Exploration**
    
    This multipage Streamlit application allows users to:
    - Visualize angles on a unit circle.
    - Compute and view trigonometric function values (sine, cosine, tangent, cosecant, secant, and cotangent).
    - Explore interactive charts that show how these values change with the angle.
    
    The lab is designed to provide both a theoretical and practical insight into trigonometric functions, linked to concepts in advanced mathematics. Detailed explanations, formulas, and real-time visualizations help reinforce learning.
    """)
    st.write("Use the sidebar to navigate between pages and adjust the settings interactively.")
    
else:
    st.write("Select a page from the sidebar.")

# End of app.py

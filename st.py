import streamlit as st

# Create a list of curve types and their corresponding constants
curve_types = {
    "IEC standard inverse": (0.140, 0.020),
    "IEC very inverse": (13.5, 1),
    "IEC extremely inverse": (80, 2),
    "IEC long time standard inverse": (120, 1)
}

# Get user input for TMS, I, Is, and curve type
tms = st.number_input("Enter TMS:")
actual_current = st.number_input("Enter I:")
is_setting = st.number_input("Enter Is:")

# Create a dropdown menu for curve type selection
curve_type = st.selectbox("Select curve type:", list(curve_types.keys()))

# Get the constants for the selected curve type
k, alpha = curve_types[curve_type]

# Calculate trip time
trip_time = tms * (k / (actual_current / is_setting) ** alpha - 1)

# Print the trip time output
st.write("Trip time:", trip_time, "seconds")

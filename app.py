import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Title
st.title("⚙️ Mechanical Unit Converter and Material Density Checker")

# Student Information
st.markdown("## 👨‍🎓 Student Information")
st.write("**Full Name:** Farhan Ali Shahid")
st.write("**Roll Number:** 25-ME-204")

st.markdown("---")

# =========================
# UNIT CONVERTER
# =========================

st.header("🔄 Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Mass", "Temperature"]
)

# Length Conversion
if conversion_type == "Length":
    meter = st.number_input("Enter value in meters", min_value=0.0)

    cm = meter * 100
    mm = meter * 1000
    feet = meter * 3.28084

    st.success(f"Centimeters: {cm:.2f} cm")
    st.success(f"Millimeters: {mm:.2f} mm")
    st.success(f"Feet: {feet:.2f} ft")

# Mass Conversion
elif conversion_type == "Mass":
    kg = st.number_input("Enter value in kilograms", min_value=0.0)

    grams = kg * 1000
    pounds = kg * 2.20462

    st.success(f"Grams: {grams:.2f} g")
    st.success(f"Pounds: {pounds:.2f} lb")

# Temperature Conversion
elif conversion_type == "Temperature":
    celsius = st.number_input("Enter temperature in Celsius")

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
    st.success(f"Kelvin: {kelvin:.2f} K")

st.markdown("---")

# =========================
# MATERIAL DENSITY CHECKER
# =========================

st.header("🧱 Material Density Checker")

materials = {
    "Aluminum": 2700,
    "Steel": 7850,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500
}

material = st.selectbox("Select Material", list(materials.keys()))

density = materials[material]

st.info(f"Density of {material}: {density} kg/m³")

# Footer
st.markdown("---")
st.caption("Developed using Streamlit Cloud and GitHub")

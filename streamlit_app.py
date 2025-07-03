
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("risk_data.csv")

st.set_page_config(layout="wide")
st.title("🦟 PathoCast: Dengue Risk Dashboard for Lahore")
st.markdown("""
This interactive MVP visualizes simulated dengue outbreak risk across Lahore based on geospatial clustering.
No personal or proprietary modeling code is exposed in this version. All data is synthetically generated.
""")

# Show map
st.subheader("📍 Geographic Risk Map (Simulated Data)")
st.map(df[['latitude', 'longitude']])

# Show summary table
st.subheader("📊 Summary by Risk Level")
st.write(df['risk_level'].value_counts().rename({0: "Low", 1: "Medium", 2: "High"}))

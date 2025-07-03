
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



# SMS ALERT DEMO 

st.markdown("---")
st.header("📲 Simulated SMS Alert Preview")

# User inputs (simulated data)
location = st.selectbox("District", ["Gulberg", "Ravi", "Iqbal", "Shalimar"])
risk_level = st.select_slider("Predicted Risk Level", options=[0, 1, 2], value=1)

# Fake SMS preview
if st.button("Generate SMS Alert"):
    alert = f"📡 PathoCast Alert: Dengue Risk Level {risk_level} in {location}. Follow prevention protocols. - Public Health Dept"
    st.success("SMS Alert Sent:")
    st.code(alert)



# DASHBOARD TABLE FILTER

st.markdown("---")
st.header("📈 Filtered Risk Table (Optional)")

risk_filter = st.selectbox("Show only this risk level", [None, 0, 1, 2])

filtered_df = df if risk_filter is None else df[df["risk_level"] == risk_filter]
st.dataframe(filtered_df)


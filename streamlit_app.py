!pip install streamlit-folium 
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

# Map
import folium
from streamlit_folium import st_folium

st.subheader("Geographic Risk Map (Simulated Data)")

m = folium.Map(location=[31.5, 74.3], zoom_start=11)

for _, row in df.iterrows():
    risk = row["risk_level"]
    color = "green" if risk == 0 else "orange" if risk == 1 else "red"
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5,
        popup=f"Risk Level: {risk}",
        color=color,
        fill=True,
        fill_opacity=0.7
    ).add_to(m)

st_folium(m, width=700, height=450)


# Summary table
st.subheader("Summary by Risk Level")
st.write(df['risk_level'].value_counts().rename({0: "Low", 1: "Medium", 2: "High"}))



# SMS ALERT DEMO 

st.markdown("---")
st.header("Simulated SMS Alert Preview")

# User inputs (simulated data)
location = st.selectbox("District", ["Gulberg", "Ravi", "Iqbal", "Shalimar"])
risk_level = st.select_slider("Predicted Risk Level", options=[0, 1, 2], value=1)

# Fake SMS preview
if st.button("Generate SMS Alert"):
    alert = f"PathoCast Alert: Dengue Risk Level {risk_level} in {location}. Follow prevention protocols. - Public Health Dept"
    st.success("SMS Alert Sent:")
    st.code(alert)

st.markdown("📲 **Realistic SMS Preview**")

with st.chat_message("assistant"):
    st.markdown(f"""
     **PathoCast Alert**  
    Dengue Risk Level **{risk_level}** detected in **{location}**.  
    Please initiate preventive measures and inform local clinics.  
    — Public Health Command Center
    """)


# DASHBOARD TABLE FILTER

st.markdown("---")
st.header("Filtered Risk Table")

risk_filter = st.selectbox("Show only this risk level", [None, 0, 1, 2])

filtered_df = df if risk_filter is None else df[df["risk_level"] == risk_filter]
st.dataframe(filtered_df)





st.subheader("Risk Trend Over Time")

trend = df.groupby("date")["risk_level"].mean().reset_index()
st.line_chart(trend.set_index("date"))

import streamlit as st

st.title("Prediction Dashboard")

product = st.selectbox("Product type", ["Tomato", "Strawberry", "Orange", "Olive"])
temp = st.number_input("Temperature (°C)", min_value=-5.0, max_value=40.0, value=9.0)
hum = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=85.0)
days = st.number_input("Storage duration (days)", min_value=0, max_value=30, value=4)
price = st.number_input("Current price (MAD / kg)", min_value=0.0, value=12.0)

st.divider()

st.subheader("Result (POC placeholder)")
# Placeholder logic for Day 1 — replace with model later
risk_prob = min(0.95, max(0.05, 0.15 + (hum/100)*0.4 + (days/10)*0.3 + (temp/20)*0.2))
risk_pct = int(risk_prob * 100)

if risk_pct >= 70:
    risk_level = "High"
elif risk_pct >= 40:
    risk_level = "Medium"
else:
    risk_level = "Low"

st.write(f"**Risk level:** {risk_level}")
st.progress(risk_prob)
st.write(f"**Spoilage probability:** {risk_pct}%")

st.subheader("Suggested action (POC)")
if risk_level == "High":
    st.write("- Apply markdown (10–20%)\n- Prioritize display\n- Transfer to faster-selling area")
elif risk_level == "Medium":
    st.write("- Monitor closely\n- Prioritize rotation (FIFO)\n- Consider small markdown")
else:
    st.write("- Normal rotation\n- Continue monitoring")
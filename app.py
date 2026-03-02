import streamlit as st

# ---- CONFIG ----
st.set_page_config(page_title="Monqida POC", page_icon="🍅", layout="wide")

# ---- SIMPLE PASSWORD GATE ----
ACCESS_CODE = "MONQIDA2026"   # change this
code = st.text_input("Enter access code", type="password")
if code != ACCESS_CODE:
    st.info("Access restricted. Enter the code provided during the hackathon.")
    st.stop()

# ---- HOME ----
st.title("Monqida 🍅")
st.subheader("AI-powered spoilage risk prediction for fresh produce")
st.write(
    "Monqida helps retailers anticipate spoilage and take early actions "
    "(markdown, transfer, prioritize sale) to reduce shrink and recover revenue."
)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Baseline shrink", "35%")
with col2:
    st.metric("Target reduction (pilot)", "10–15%")
with col3:
    st.metric("Goal", "Less waste, higher margin")

st.divider()
st.write("Use the **Dashboard** to enter conditions and get a spoilage risk prediction.")
st.write("Use **Insights** to review history and financial impact (POC).")
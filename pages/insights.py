import streamlit as st
import pandas as pd


st.title("Insights (POC)")

if "history" in st.session_state and len(st.session_state.history) > 0:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df)

    total_recovered = df["Recovered MAD/kg"].sum()
    st.metric("Total Recovered (MAD/kg cumulative)", f"{total_recovered:.2f}")
else:
    st.info("No predictions saved yet.")
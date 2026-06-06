import streamlit as st
import pandas as pd

st.set_page_config(page_title="IPL 2008 Auction", layout="wide")

st.title("IPL 2008 Auction Dashboard")
st.subheader("Week 2 Project 1 - Roll No: 25JR5A0527-Bindu")

# Load CSV file
df = pd.read_csv("IPL.csv")

st.write("### Player Data")
st.dataframe(df, use_container_width=True)

st.write("### Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Players", len(df))
col2.metric("Total Runs", int(df['Runs'].sum()))
col3.metric("Avg Price", f"{df['Price'].mean():.0f}L")

st.write("---")
st.caption("TDS Mini Hackathon - Created by Bindu")

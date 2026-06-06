import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IPL 2008 Auction Dashboard", layout="wide")
st.title("🏏 IPL 2008 Auction - AI Dashboard")
st.caption("Roll No: 25JR5A0527_Bindu | Week 2 Project 1")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/atulpatelDS/CSV-ML-Data-Files-Download/master/IPL-2008-Dataset.csv"
    df = pd.read_csv(url)
    df['PRICE'] = df['PRICE'].astype(str).str.replace(',', '').str.strip()
    def convert_price(x):
        x = x.upper()
        if 'CR' in x: return float(x.replace('CR', ''))
        elif 'LAC' in x: return float(x.replace('LAC', '')) / 100
        else: return float(x)
    df['PRICE_CR'] = df['PRICE'].apply(convert_price)
    df = df.fillna('Unknown')
    return df

df = load_data()

st.sidebar.header("Filters")
teams = st.sidebar.multiselect("Select Team", options=df['TEAM'].unique(), default=df['TEAM'].unique())
roles = st.sidebar.multiselect("Select Player Type", options=df['TYPE'].unique(), default=df['TYPE'].unique())
df_filtered = df[df['TEAM'].isin(teams) & df['TYPE'].isin(roles)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Players", df_filtered.shape[0])
col2.metric("Total Teams", df_filtered['TEAM'].nunique())
col3.metric("Highest Bid", f"{df_filtered['PRICE_CR'].max()} Cr")
col4.metric("Indian Players", df_filtered[df_filtered['COUNTRY'] == 'IND'].shape[0])

st.subheader("1. Total Spending by Team")
fig1 = px.bar(df_filtered.groupby('TEAM')['PRICE_CR'].sum().reset_index(), x='TEAM', y='PRICE_CR', color='TEAM')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("2. Top 10 Most Expensive Players")
fig2 = px.bar(df_filtered.nlargest(10, 'PRICE_CR'), x='PLAYER', y='PRICE_CR', color='TEAM')
st.plotly_chart(fig2, use_container_width=True)

st.subheader("3. Price Distribution by Player Type")
fig3 = px.box(df_filtered, x='TYPE', y='PRICE_CR', color='TYPE')
st.plotly_chart(fig3, use_container_width=True)

st.subheader("4. Players by Country")
fig4 = px.pie(df_filtered, names='COUNTRY', hole=0.3)
st.plotly_chart(fig4, use_container_width=True)

st.subheader("5. Total Players per Team")
fig5 = px.bar(df_filtered['TEAM'].value_counts().reset_index(), x='TEAM', y='count', color='TEAM')
st.plotly_chart(fig5, use_container_width=True)

st.subheader("📋 Cleaned Dataset")
st.dataframe(df_filtered)
st.download_button("Download CSV", df_filtered.to_csv(index=False), "ipl_2008_cleaned.csv")

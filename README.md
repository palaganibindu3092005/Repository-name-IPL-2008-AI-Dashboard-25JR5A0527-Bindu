# 🏏 IPL 2008 Auction - AI Dashboard
**Roll No:** 25JR5A0527_Bindu  
**Internship:** Week 2 Final Assignment - Project 1

## 📊 Project Overview
Interactive Streamlit dashboard analyzing IPL 2008 Auction data with 5 visualizations, data cleaning, KPIs, and filters.

## ✨ Features Covered
1. **Dataset Overview** - Total Players: 77, Total Teams: 8
2. **Data Cleaning** - Handled missing values, Price conversion Cr/Lac to float
3. **Key Metrics** - Highest Bid: 9.5 Cr MS Dhoni, Total Teams, Indian Players count
4. **Interactive Filters** - Filter by Team and Player Role/Type
5. **5 Visualizations:**
   - Total Spending by Team - Bar Chart
   - Top 10 Most Expensive Players - Bar Chart  
   - Price Distribution by Player Type - Box Plot
   - Players by Country - Pie Chart
   - Total Players per Team - Bar Chart
6. **Download** - Export cleaned data as CSV

## 🛠️ Tech Stack
Python, Streamlit, Pandas, Plotly Express

## 📁 Dataset
**Source:** IPL 2008 Auction Dataset  
**Link:** https://raw.githubusercontent.com/atulpatelDS/CSV-ML-Data-Files-Download/master/IPL-2008-Dataset.csv

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run main.py

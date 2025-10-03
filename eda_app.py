import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_dataset.csv")

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Add revenue column
df['revenue'] = df['quantity'] * df['price'] * (1 - df['discount'])

st.title("E-Commerce Data Analysis Dashboard")

# Graph 5: Payment Method Distribution
st.subheader("Graph 5: Payment Method Distribution")
payment_counts = df['payment_method'].value_counts()
st.bar_chart(payment_counts)

# Graph 6: Sales by Region
st.subheader("Graph 6: Total Revenue by Region")
region_sales = df.groupby('region')['revenue'].sum().sort_values()
st.bar_chart(region_sales)

# Time Series Graph 1: Total Sales Over Time
st.subheader("Time Series 1: Total Revenue Over Time")
daily_sales = df.groupby(df['order_date'].dt.date)['revenue'].sum()
st.line_chart(daily_sales)

# Time Series Graph 2: Sales by Category Over Time
st.subheader("Time Series 2: Revenue by Category Over Time")
category_sales = df.groupby([df['order_date'].dt.to_period("M"), 'category'])['revenue'].sum().unstack()
st.line_chart(category_sales)

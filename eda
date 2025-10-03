import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_dataset.csv")

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Add a revenue column
df['revenue'] = df['quantity'] * df['price'] * (1 - df['discount'])

st.title("E-Commerce Data Analysis Dashboard")

# Graph 5: Payment Method Distribution (Pie Chart)
st.subheader("Graph 5: Payment Method Distribution")
payment_counts = df['payment_method'].value_counts()
fig5, ax5 = plt.subplots()
ax5.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90)
ax5.axis('equal')
st.pyplot(fig5)

# Graph 6: Sales by Region (Bar Chart)
st.subheader("Graph 6: Total Revenue by Region")
region_sales = df.groupby('region')['revenue'].sum().sort_values()
fig6, ax6 = plt.subplots()
region_sales.plot(kind='bar', ax=ax6)
ax6.set_ylabel("Revenue")
ax6.set_xlabel("Region")
st.pyplot(fig6)

# Time Series Graph 1: Total Sales Over Time
st.subheader("Time Series 1: Total Revenue Over Time")
daily_sales = df.groupby(df['order_date'].dt.date)['revenue'].sum()
fig7, ax7 = plt.subplots()
daily_sales.plot(ax=ax7)
ax7.set_ylabel("Revenue")
ax7.set_xlabel("Date")
st.pyplot(fig7)

# Time Series Graph 2: Sales by Category Over Time
st.subheader("Time Series 2: Revenue by Category Over Time")
category_sales = df.groupby([df['order_date'].dt.to_period("M"), 'category'])['revenue'].sum().unstack()
fig8, ax8 = plt.subplots()
category_sales.plot(ax=ax8)
ax8.set_ylabel("Revenue")
ax8.set_xlabel("Month")
st.pyplot(fig8)

import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_dataset.csv")

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Add revenue column
df['revenue'] = df['quantity'] * df['price'] * (1 - df['discount'])

st.title("E-Commerce Data Analysis Dashboard")

# -----------------------------
# Graph 1: Top 10 Selling Products
st.subheader("Graph 1: Top 10 Selling Products")
top_products = df.groupby('product_id')['quantity'].sum().nlargest(10)
st.bar_chart(top_products)

# Graph 2: Revenue by Product Category
st.subheader("Graph 2: Revenue by Product Category")
category_revenue = df.groupby('category')['revenue'].sum().sort_values()
st.bar_chart(category_revenue)

# Graph 3: Average Order Value by Region
st.subheader("Graph 3: Average Order Value by Region")
aov_region = df.groupby('region')['revenue'].mean()
st.bar_chart(aov_region)

# Graph 4: Discounts Distribution
st.subheader("Graph 4: Discount Distribution")
st.histogram(df['discount']) if hasattr(st, "histogram") else st.line_chart(df['discount'].value_counts())

# Graph 5: Payment Method Distribution
st.subheader("Graph 5: Payment Method Distribution")
payment_counts = df['payment_method'].value_counts()
st.bar_chart(payment_counts)

# Graph 6: Total Revenue by Region
st.subheader("Graph 6: Total Revenue by Region")
region_sales = df.groupby('region')['revenue'].sum().sort_values()
st.bar_chart(region_sales)

# Graph 7 (Time Series 1): Total Revenue Over Time
st.subheader("Graph 7: Total Revenue Over Time")
daily_sales = df.groupby(df['order_date'].dt.date)['revenue'].sum()
st.line_chart(daily_sales)

# Graph 8 (Time Series 2): Revenue by Category Over Time
st.subheader("Graph 8: Revenue by Category Over Time")
category_sales = df.groupby([df['order_date'].dt.to_period("M"), 'category'])['revenue'].sum().unstack()
st.line_chart(category_sales)

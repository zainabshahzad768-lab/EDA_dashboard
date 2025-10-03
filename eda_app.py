import streamlit as st
import pandas as pd
import altair as alt  # comes with Streamlit

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

# ✅ Graph 2: Revenue Share by Category (Pie Chart using Altair)
st.subheader("Graph 2: Revenue Share by Category (Altair Pie)")
category_revenue = df.groupby('category')['revenue'].sum().reset_index()

pie_chart = alt.Chart(category_revenue).mark_arc().encode(
    theta="revenue",
    color="category",
    tooltip=["category", "revenue"]
)

st.altair_chart(pie_chart, use_container_width=True)

# Graph 3: Average Order Value by Region
st.subheader("Graph 3: Average Order Value by Region")
aov_region = df.groupby('region')['revenue'].mean()
st.bar_chart(aov_region)

# Graph 4: Discounts Distribution
st.subheader("Graph 4: Discount Distribution")
st.bar_chart(df['discount'].value_counts().sort_index())

# ✅ Graph 5: Payment Method Distribution (Altair Pie)
st.subheader("Graph 5: Payment Method Distribution (Altair Pie)")
payment_counts = df['payment_method'].value_counts().reset_index()
payment_counts.columns = ["payment_method", "count"]

pie_chart2 = alt.Chart(payment_counts).mark_arc().encode(
    theta="count",
    color="payment_method",
    tooltip=["payment_method", "count"]
)

st.altair_chart(pie_chart2, use_container_width=True)

# Graph 6: Total Revenue by Region
st.subheader("Graph 6: Total Revenue by Region")
region_sales = df.groupby('region')['revenue'].sum().sort_values()
st.bar_chart(region_sales)

# Graph 7: Total Revenue Over Time
st.subheader("Graph 7: Total Revenue Over Time")
daily_sales = df.groupby(df['order_date'].dt.date)['revenue'].sum()
st.line_chart(daily_sales)

# Graph 8: Revenue by Category Over Time
st.subheader("Graph 8: Revenue by Category Over Time")
category_sales = df.groupby([df['order_date'].dt.to_period("M"), 'category'])['revenue'].sum().unstack()
st.line_chart(category_sales)

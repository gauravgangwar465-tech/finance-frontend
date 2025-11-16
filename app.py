import streamlit as st
import requests
import pandas as pd

API_URL = "https://backend-finance-vspr.onrender.com"

st.title("💰 Personal Finance Companion")

# Expense Input
st.header("Add Expense")
amount = st.number_input("Amount", min_value=1)
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
note = st.text_input("Note")

if st.button("Add Expense"):
    data = {
        "amount": amount,
        "category": category,
        "note": note
    }
    try:
        r = requests.post(f"{API_URL}/add-expense", json=data)
        st.success("Expense Added Successfully!")
    except:
        st.error("Backend not reachable")

# Dashboard
st.header("📊 Dashboard")
try:
    r = requests.get(f"{API_URL}/expenses")
    expenses = r.json()

    df = pd.DataFrame(expenses)
    st.write(df)

    chart_df = df.groupby("category")["amount"].sum()
    st.bar_chart(chart_df)

except:
    st.warning("Unable to fetch dashboard data")

import streamlit as st
import requests

BACKEND_URL = "https://backend-finance-mu-three.vercel.app"

st.title("💰 Personal Finance Dashboard")

menu = st.sidebar.selectbox("Menu", ["Home", "Add Expense", "View Expenses"])

if menu == "Home":
    st.write("Welcome to your finance dashboard!")

elif menu == "Add Expense":
    st.header("Add Expense")

    amount = st.number_input("Amount", min_value=1)
    category = st.selectbox("Category", ["Food", "Travel", "Bills", "Shopping"])
    note = st.text_input("Note")

    if st.button("Save Expense"):
        data = {
            "amount": amount,
            "category": category,
            "note": note
        }
        res = requests.post(f"{BACKEND_URL}/expense", json=data)

        if res.status_code == 200:
            st.success("Expense saved!")
        else:
            st.error("Failed to save expense")

elif menu == "View Expenses":
    st.header("All Expenses")

    res = requests.get(f"{BACKEND_URL}/expenses")
    if res.status_code == 200:
        st.table(res.json())
    else:
        st.error("Could not load expenses")

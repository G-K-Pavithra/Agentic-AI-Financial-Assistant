import streamlit as st
import pandas as pd

from agentic_ai import agentic_finance_agent

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Agentic AI Financial Assistant Dashboard", layout="wide")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("personal_finance_dataset_8000_extended.csv")

# -----------------------------
# TITLE
# -----------------------------
st.title("Agentic AI Financial Assistant")
st.write("Welcome to your Agentic AI Financial Assistant Dashboard")

# -----------------------------
# BASIC METRICS
# -----------------------------
total_expense = df["Amount"].sum()
avg_expense = df["Amount"].mean()
total_transactions = len(df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Expense", f"₹{total_expense:,.0f}")

with col2:
    st.metric("Average Expense", f"₹{avg_expense:,.0f}")

with col3:
    st.metric("Transactions", total_transactions)

st.divider()

# -----------------------------
# DATA PREVIEW
# -----------------------------
with st.expander("📂 View Dataset"):
    st.dataframe(df)

# -----------------------------
# CATEGORY SPENDING
# -----------------------------
st.subheader("Category-wise Spending")

if "Category" in df.columns:
    category_data = df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_data)

# -----------------------------
# MONTHLY TREND
# -----------------------------
st.subheader("Monthly Spending Trend")

if "Month" in df.columns:
    monthly_data = df.groupby("Month")["Amount"].sum()
    st.line_chart(monthly_data)

# -----------------------------
# PAYMENT METHOD
# -----------------------------
import plotly.express as px

st.subheader("Payment Method Distribution")

if "PaymentMethod" in df.columns:

    payment = df.groupby("PaymentMethod")["Amount"].sum()

    fig = px.pie(
        values=payment.values,
        names=payment.index,
        title="Payment Method Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("PaymentMethod column not found.")

# -----------------------------
# AI SECTION
# -----------------------------

st.subheader("🤖 Ask Finance AI")

st.info("""
Try asking:

* What is my total spending?

* Which category has the highest spending?

* Show monthly spending.

* Which location has the highest spending?

* Suggest ways to reduce my expenses.
""")

question = st.text_input("Ask anything about your spending")

if st.button("Ask AI"):
    if question:
        try:
            answer = agentic_finance_agent(df, question)
            st.success(answer)
        except Exception as e:
            st.error(f"AI Error: {e}")
    else:
        st.warning("Please enter a question")

        st.markdown("---")
st.caption("Developed by Pavithra GK | Agentic AI Proof of Concept")
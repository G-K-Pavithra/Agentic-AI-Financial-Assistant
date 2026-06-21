from tools import *

AED_RATE = 0.044   # 1 INR ≈ 0.044 AED

def finance_agent(question):

    q = question.lower()

    if "total expense" in q or "total spending" in q:
        return total_spending()

    elif "highest expense" in q or "maximum expense" in q:
        return f"Highest Expense: ₹{df['Amount'].max():,.2f}"

    elif "lowest expense" in q or "minimum expense" in q:
        return f"Lowest Expense: ₹{df['Amount'].min():,.2f}"

    elif "average expense" in q:
        return f"Average Expense: ₹{df['Amount'].mean():,.2f}"

    elif "category" in q and "spending" in q:
        return spending_by_category()

    elif "top category" in q or "highest category" in q:
        cat = df.groupby("Category")["Amount"].sum().idxmax()
        amt = df.groupby("Category")["Amount"].sum().max()
        return f"Top Spending Category: {cat} (₹{amt:,.2f})"

    elif "month" in q and "spending" in q:
        return df.groupby("Month")["Amount"].sum()

    elif "highest month" in q or "month has highest" in q:
        month = df.groupby("Month")["Amount"].sum().idxmax()
        amount = df.groupby("Month")["Amount"].sum().max()
        return f"{month} has the highest spending (₹{amount:,.2f})"

    elif "transactions" in q:
        return f"Total Transactions: {len(df)}"

    elif "financial summary" in q:
        return f"""
Financial Summary

Total Transactions : {len(df)}
Total Spending : ₹{df['Amount'].sum():,.2f}
Highest Expense : ₹{df['Amount'].max():,.2f}
Lowest Expense : ₹{df['Amount'].min():,.2f}
Average Expense : ₹{df['Amount'].mean():,.2f}
Top Category : {df.groupby('Category')['Amount'].sum().idxmax()}
"""

    elif "reduce" in q or "save money" in q:
        top = df.groupby("Category")["Amount"].sum().idxmax()
        return f"You spend the most on {top}. Reducing expenses in this category could help you save more."

    elif "aed" in q:
        df_copy = df.copy()
        df_copy["Amount"] = df_copy["Amount"] * AED_RATE
        return df_copy[["Description","Amount"]].head(20)

    elif "inr" in q:
        return "All amounts are already stored in INR."

    else:
        return "Sorry, I couldn't understand the question."
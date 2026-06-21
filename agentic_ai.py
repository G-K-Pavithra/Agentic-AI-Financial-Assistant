import pandas as pd

def analyze_intent(question):
    q=question.lower()
    if "month" in q or "monthly" in q: return "monthly_trend"
    elif "week" in q or "weekday" in q or "day" in q: return "weekday_spending"
    elif "time" in q or "morning" in q or "afternoon" in q or "evening" in q or "night" in q: return "time_spending"
    elif "location" in q or "place" in q or "city" in q or "where" in q: return "location_spending"
    elif "payment" in q: return "payment_spending"
    elif "category" in q: return "category_spending"
    elif "average" in q: return "average_spending"
    elif "transaction" in q: return "transactions"
    elif "total" in q: return "total_spending"
    elif "highest" in q or "top" in q: return "top_expense"
    elif "reduce" in q or "save" in q: return "savings_advice"
    return "general_summary"

def agentic_finance_agent(df,question):
    intent=analyze_intent(question)
    if intent=="total_spending":
        return f"Your total spending is ₹{df['Amount'].sum():,.0f}"
    elif intent=="average_spending":
        return f"Average spending is ₹{df['Amount'].mean():,.0f}"
    elif intent=="transactions":
        return f"Total transactions: {len(df)}"
    elif intent=="category_spending":
        return df.groupby("Category")["Amount"].sum().sort_values(ascending=False).to_string()
    elif intent=="top_expense":
        s=df.groupby("Category")["Amount"].sum()
        return f"Highest spending category is {s.idxmax()} with ₹{s.max():,.0f}"
    elif intent=="monthly_trend":
        s=df.groupby("Month")["Amount"].sum()
        return f"Highest Spending Month: {s.idxmax()}\nAmount: ₹{s.max():,.0f}\n\nMonthly Spending Summary:\n\n{s.to_string()}"
    elif intent=="weekday_spending":
        if "Weekday" not in df.columns: return "Weekday column not found."
        s=df.groupby("Weekday")["Amount"].sum()
        return f"Highest Spending Weekday: {s.idxmax()}\nAmount: ₹{s.max():,.0f}\n\n{s.to_string()}"
    elif intent=="time_spending":
        if "TimeOfDay" not in df.columns: return "TimeOfDay column not found."
        s=df.groupby("TimeOfDay")["Amount"].sum()
        return f"Highest Spending Time: {s.idxmax()}\nAmount: ₹{s.max():,.0f}\n\n{s.to_string()}"
    elif intent=="location_spending":
        if "Location" not in df.columns: return "Location column not found."
        s=df.groupby("Location")["Amount"].sum().sort_values(ascending=False)
        return f"Highest Spending Location: {s.index[0]}\nAmount: ₹{s.iloc[0]:,.0f}\n\n{s.head().to_string()}"
    elif intent=="payment_spending":
        if "PaymentMethod" not in df.columns: return "PaymentMethod column not found."
        s=df.groupby("PaymentMethod")["Amount"].sum()
        return f"Most Used Payment Method: {s.idxmax()}\nAmount: ₹{s.max():,.0f}\n\n{s.to_string()}"
    elif intent=="savings_advice":
        top=df.groupby("Category")["Amount"].sum().idxmax()
        return f"Savings Recommendations\n\n• Highest spending category: {top}\n• Set a monthly budget.\n• Track daily expenses.\n• Reduce spending in your highest category."
    total=df["Amount"].sum()
    cats=df["Category"].nunique()
    top=df.groupby("Category")["Amount"].sum().idxmax()
    return f"Financial Summary\n\nTotal Spending: ₹{total:,.0f}\nCategories: {cats}\nTop Category: {top}"
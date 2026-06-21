print("Hello! Finance Agent is starting...")
from tools import dataset_summary

print(dataset_summary())
from tools import *

print("Total Spending")
print(total_spending())

print("\nCategory-wise Spending")
print(spending_by_category())

print("\nLocation-wise Spending")
print(spending_by_location())

print("\nPayment Method-wise Spending")
print(spending_by_payment())
from agent import finance_agent

print("===== Personal Finance Agent =====")

while True:
    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    answer = finance_agent(question)
    print("\nAnswer:")
    print(answer)
print("\n=== Savings Classification ===")
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
savings = income - expenses

if savings > 10000:
    status = "Saving Well"
elif savings >= 5000:
    status = "Average"
else:
    status = "Try to Save"

print(f"Savings: {savings}, Status: {status}")

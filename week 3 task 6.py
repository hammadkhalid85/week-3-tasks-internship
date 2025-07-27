print("\n=== Billing System ===")
products = int(input("Enter number of products: "))
price = float(input("Enter total price: "))

if price > 1000 and products > 3:
    discount = 0.15  # 15%
elif price > 500:
    discount = 0.10  # 10%
else:
    discount = 0.0

final_bill = price - (price * discount)
print(f"Discount: {discount*100:.0f}%, Final Bill: {final_bill}")

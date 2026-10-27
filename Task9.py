
# Multi-Product Shopping Budget Constraint

budget = float(input("Enter your shopping budget (Rs.): "))
n = int(input("Enter number of products: "))

if budget < 0 or n <= 0:
    print("Invalid budget or number of products!")

else:
    products = []
    subtotal = 0

    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        price = float(input("Enter price per item (Rs.): "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("Invalid price or quantity!")
            continue

        cost = price * quantity
        subtotal += cost

        products.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "cost": cost
        })

    # Discount conditions
    if subtotal >= 5000:
        discount_rate = 0.15
    elif subtotal >= 2000:
        discount_rate = 0.10
    elif subtotal >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = subtotal * discount_rate
    total = subtotal - discount

    print("\n====== SHOPPING BILL ======")
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount:", discount_rate * 100, "%")
    print("Discount amount: Rs.", round(discount, 2))
    print("Final amount: Rs.", round(total, 2))
    print("Budget: Rs.", round(budget, 2))

    # Reduce quantities if the budget is exceeded
    if total <= budget:
        print("\nYour shopping is within budget!")
    else:
        print("\nBudget exceeded by Rs.", round(total - budget, 2))
        print("Suggested quantity reductions:")

        # Reduce the most expensive items first
        products.sort(key=lambda p: p["price"], reverse=True)

        while True:
            subtotal = sum(p["price"] * p["quantity"] for p in products)

            if subtotal >= 5000:
                rate = 0.15
            elif subtotal >= 2000:
                rate = 0.10
            elif subtotal >= 1000:
                rate = 0.05
            else:
                rate = 0

            total = subtotal * (1 - rate)

            if total <= budget:
                break

            # Find the most expensive product with quantity remaining
            item = next(
                (p for p in products if p["quantity"] > 0),
                None
            )

            if item is None:
                break

            item["quantity"] -= 1
            print("Reduce", item["name"], "by 1 item.")

        print("\n====== REVISED SHOPPING LIST ======")

        for p in products:
            print(p["name"], "- Quantity:", p["quantity"])

        print("Revised subtotal: Rs.", round(subtotal, 2))
        print("Revised discount: Rs.", round(subtotal * rate, 2))
        print("Revised total: Rs.", round(total, 2))
        print("Remaining budget: Rs.", round(budget - total, 2))

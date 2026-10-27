
# Warehouse Inventory Reconciliation

products = int(input("Enter number of products: "))

if products <= 0:
    print("Invalid number of products!")
else:
    total_discrepancies = 0
    total_replenishment = 0

    for i in range(1, products + 1):
        print("\n--- Product", i, "---")

        name = input("Enter product name: ")
        opening = int(input("Enter opening stock: "))
        incoming = int(input("Enter incoming quantity: "))
        dispatched = int(input("Enter dispatched quantity: "))
        closing = int(input("Enter actual closing stock: "))
        minimum_stock = int(input("Enter minimum stock required: "))

        # Validate inventory quantities
        if min(opening, incoming, dispatched,
               closing, minimum_stock) < 0:
            print("Invalid quantities! Values cannot be negative.")
            continue

        # Calculate expected closing stock
        expected = opening + incoming - dispatched

        # Calculate discrepancy
        discrepancy = closing - expected

        # Calculate replenishment requirement
        replenishment = max(0, minimum_stock - closing)

        print("\nProduct Name:", name)
        print("Expected Closing Stock:", expected)
        print("Actual Closing Stock:", closing)

        if discrepancy == 0:
            print("Stock Status: Reconciled")
        elif discrepancy > 0:
            print("Discrepancy:", discrepancy, "extra units")
            print("Stock Status: Surplus")
            total_discrepancies += abs(discrepancy)
        else:
            print("Discrepancy:", abs(discrepancy), "missing units")
            print("Stock Status: Shortage")
            total_discrepancies += abs(discrepancy)

        print("Replenishment Required:", replenishment, "units")

        total_replenishment += replenishment

    print("\n====== WAREHOUSE SUMMARY ======")
    print("Total discrepancy units:", total_discrepancies)
    print("Total replenishment required:", total_replenishment)
    print("================================")


# Multi-Day Water Tank Simulation

capacity = float(input("Enter tank capacity (litres): "))
initial_water = float(input("Enter initial water level (litres): "))
threshold = float(input("Enter target water level (litres): "))
days = int(input("Enter number of days: "))

if (capacity <= 0 or initial_water < 0
        or initial_water > capacity
        or threshold < 0 or threshold > capacity
        or days <= 0):
    print("Invalid input values!")

else:
    water = initial_water
    overflow_total = 0
    shortage_total = 0
    first_threshold_day = None

    for day in range(1, days + 1):
        print("\nDay", day)

        inflow = float(input("Enter water inflow (litres): "))
        outflow = float(input("Enter water outflow (litres): "))

        if inflow < 0 or outflow < 0:
            print("Invalid quantities! Enter non-negative values.")
            continue

        # Calculate water level before applying tank limits
        new_level = water + inflow - outflow

        # Detect overflow
        if new_level > capacity:
            overflow = new_level - capacity
            overflow_total += overflow
            water = capacity
            print("Overflow detected:", overflow, "litres")

        # Detect shortage
        elif new_level < 0:
            shortage = abs(new_level)
            shortage_total += shortage
            water = 0
            print("Water shortage:", shortage, "litres")

        else:
            water = new_level
            print("No overflow or shortage.")

        print("Current water level:", water, "litres")

        # Find first day the threshold is reached
        if first_threshold_day is None and water >= threshold:
            first_threshold_day = day
            print("Target threshold reached on day", day)

    print("\n====== SIMULATION SUMMARY ======")
    print("Final water level:", water, "litres")
    print("Total overflow:", overflow_total, "litres")
    print("Total shortage:", shortage_total, "litres")

    if first_threshold_day is not None:
        print("First threshold reached on day:", first_threshold_day)
    else:
        print("Threshold was not reached.")

    print("================================")

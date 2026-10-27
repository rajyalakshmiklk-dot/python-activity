
# Fuel Consumption and Route Comparison

vehicles = int(input("Enter number of vehicles: "))
distance = float(input("Enter journey distance (km): "))
fuel_price = float(input("Enter fuel price per litre (Rs.): "))
reserve_percent = float(input("Enter reserve fuel percentage: "))

if (vehicles <= 0 or distance <= 0 or fuel_price <= 0
        or reserve_percent < 0):
    print("Invalid input values!")

else:
    results = []

    for i in range(vehicles):
        print("\nVehicle", i + 1)

        name = input("Enter vehicle name: ")
        mileage = float(input("Enter mileage (km/litre): "))
        tank_fuel = float(input("Enter available fuel (litres): "))

        if mileage <= 0 or tank_fuel < 0:
            print("Invalid mileage or fuel quantity. Skipping vehicle.")
            continue

        # Fuel needed for the journey
        journey_fuel = distance / mileage

        # Additional reserve fuel required
        reserve_fuel = journey_fuel * reserve_percent / 100

        # Total fuel requirement
        total_fuel = journey_fuel + reserve_fuel

        # Fuel that must be purchased
        fuel_to_buy = max(0, total_fuel - tank_fuel)

        # Total fuel cost
        cost = fuel_to_buy * fuel_price

        # Feasibility check
        if tank_fuel >= total_fuel:
            feasible = True
            print("Status: Feasible with available fuel")
        else:
            feasible = False
            print("Status: Fuel purchase required")

        print("Journey fuel:", round(journey_fuel, 2), "litres")
        print("Reserve fuel:", round(reserve_fuel, 2), "litres")
        print("Total fuel required:", round(total_fuel, 2), "litres")
        print("Fuel to purchase:", round(fuel_to_buy, 2), "litres")
        print("Additional fuel cost: Rs.", round(cost, 2))

        results.append({
            "name": name,
            "fuel": total_fuel,
            "purchase": fuel_to_buy,
            "cost": cost,
            "feasible": feasible
        })

    print("\n===== ROUTE COMPARISON SUMMARY =====")

    if not results:
        print("No valid vehicles available.")

    else:
        for v in results:
            print(
                v["name"],
                "| Fuel:", round(v["fuel"], 2), "litres",
                "| Cost: Rs.", round(v["cost"], 2),
                "| Feasible:", v["feasible"]
            )

        # Lowest-cost vehicle among those that can complete the trip
        # after purchasing any required fuel
        feasible_vehicles = [
            v for v in results
            if v["fuel"] >= 0 and v["purchase"] >= 0
        ]

        if feasible_vehicles:
            best = min(feasible_vehicles, key=lambda v: v["cost"])
            print("\nLowest-cost option:", best["name"])
            print("Fuel purchase cost: Rs.", round(best["cost"], 2))
        else:
            print("No feasible vehicle found.")

    print("====================================")


from datetime import datetime
import math

# Parking rates per hour
rates = {
    "car": 50,
    "bike": 20,
    "truck": 100
}

# Maximum parking charge per calendar day
daily_limits = {
    "car": 500,
    "bike": 200,
    "truck": 1000
}

OVERNIGHT_PENALTY = 100
LONG_STAY_PENALTY = 500
LONG_STAY_HOURS = 168  # 7 days

try:
    vehicle = input("Enter vehicle type (car/bike/truck): ").strip().lower()

    if vehicle not in rates:
        print("Error: Invalid vehicle type!")

    else:
        entry = input("Enter entry time (YYYY-MM-DD HH:MM): ")
        exit_input = input("Enter exit time (YYYY-MM-DD HH:MM): ")

        entry_time = datetime.strptime(entry, "%Y-%m-%d %H:%M")
        exit_time = datetime.strptime(exit_input, "%Y-%m-%d %H:%M")

        if exit_time <= entry_time:
            print("Error: Exit time must be after entry time.")

        else:
            duration_minutes = (
                exit_time - entry_time
            ).total_seconds() / 60

            total_hours = math.ceil(duration_minutes / 60)

            # Calculate charges separately for each calendar day
            current = entry_time
            parking_charge = 0

            while current < exit_time:
                next_midnight = current.replace(
                    hour=0, minute=0, second=0, microsecond=0
                )
                from datetime import timedelta
                next_midnight += timedelta(days=1)

                period_end = min(exit_time, next_midnight)
                minutes = (period_end - current).total_seconds() / 60
                hours = math.ceil(minutes / 60)

                daily_charge = min(
                    hours * rates[vehicle],
                    daily_limits[vehicle]
                )

                parking_charge += daily_charge
                current = period_end

            # Overnight penalty for crossing a calendar date
            overnight_penalty = 0
            if entry_time.date() != exit_time.date():
                overnight_penalty = OVERNIGHT_PENALTY

            # Long-stay penalty
            long_stay_penalty = 0
            if duration_minutes > LONG_STAY_HOURS * 60:
                long_stay_penalty = LONG_STAY_PENALTY

            total_amount = (
                parking_charge
                + overnight_penalty
                + long_stay_penalty
            )

            print("\n===== PARKING BILL =====")
            print("Vehicle type:", vehicle)
            print("Entry time:", entry_time)
            print("Exit time:", exit_time)
            print("Total parking hours:", total_hours)
            print("Parking charge: Rs.", parking_charge)
            print("Overnight penalty: Rs.", overnight_penalty)
            print("Long-stay penalty: Rs.", long_stay_penalty)
            print("Total amount: Rs.", total_amount)
            print("========================")

except ValueError:
    print("Error: Invalid date or time!")
    print("Use YYYY-MM-DD HH:MM format.")
    print("Example: 2026-10-27 09:30")

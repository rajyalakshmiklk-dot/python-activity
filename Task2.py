
# Attendance Recovery Computation

attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
threshold = float(input("Enter eligibility percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details!")
else:
    current_percentage = (attended / conducted) * 100

    print("\nCurrent Attendance:", round(current_percentage, 2), "%")

    if current_percentage >= threshold:
        print("You are already eligible!")
    else:
        print("You are not yet eligible.")

    print("\nAttendance Recovery Scenarios")

    # Scenario 1: Attend every future class
    if threshold < 100:
        required = 0
        while ((attended + required) / (conducted + required)) * 100 < threshold:
            required += 1

        print("1. Attend all future classes:")
        print("   Minimum consecutive classes required:", required)
    else:
        print("1. For 100% eligibility, all future classes")
        print("   must be attended, but past absences remain.")

    # Scenario 2: Attend 90% of future classes
    future_attendance_rate = 0.90

    print("\n2. If future attendance is 90%:")

    if threshold <= future_attendance_rate * 100:
        required = 0
        while ((attended + future_attendance_rate * required)
               / (conducted + required)) * 100 < threshold:
            required += 1

        print("   Approximate minimum future classes:", required)
    else:
        print("   The target cannot be reached with 90%")
        print("   future attendance.")

    # Scenario 3: Attend 80% of future classes
    future_attendance_rate = 0.80

    print("\n3. If future attendance is 80%:")

    if threshold <= future_attendance_rate * 100:
        required = 0
        while ((attended + future_attendance_rate * required)
               / (conducted + required)) * 100 < threshold:
            required += 1

        print("   Approximate minimum future classes:", required)
    else:
        print("   The target cannot be reached with 80%")
        print("   future attendance.")

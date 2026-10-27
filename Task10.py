
# University Admission Decision Engine

applicants = []

n = int(input("Enter number of applicants: "))

if n <= 0:
    print("Invalid number of applicants!")

else:
    print("\nAvailable courses:")
    print("1. Computer Science")
    print("2. Mechanical Engineering")
    print("3. Business Administration")

    courses = {
        "1": {
            "name": "Computer Science",
            "cutoff": 80,
            "subject": "Mathematics",
            "subject_min": 70
        },
        "2": {
            "name": "Mechanical Engineering",
            "cutoff": 70,
            "subject": "Physics",
            "subject_min": 60
        },
        "3": {
            "name": "Business Administration",
            "cutoff": 65,
            "subject": "English",
            "subject_min": 55
        }
    }

    for i in range(n):
        print("\nApplicant", i + 1)

        name = input("Enter applicant name: ")
        course_choice = input("Enter course choice (1/2/3): ")

        if course_choice not in courses:
            print("Invalid course choice. Applicant skipped.")
            continue

        course = courses[course_choice]

        aggregate = float(input("Enter aggregate percentage: "))
        subject_mark = float(
            input(f"Enter {course['subject']} percentage: ")
        )

        if not (0 <= aggregate <= 100 and 0 <= subject_mark <= 100):
            print("Invalid marks. Applicant skipped.")
            continue

        # Eligibility check
        if (aggregate >= course["cutoff"]
                and subject_mark >= course["subject_min"]):

            applicants.append({
                "name": name,
                "course": course["name"],
                "aggregate": aggregate,
                "subject_mark": subject_mark
            })

            print("Status: Eligible")
        else:
            print("Status: Not eligible")
            print("Required aggregate:", course["cutoff"], "%")
            print(
                "Required", course["subject"],
                "marks:", course["subject_min"], "%"
            )

    # Rank applicants by aggregate, then subject marks
    applicants.sort(
        key=lambda x: (x["aggregate"], x["subject_mark"]),
        reverse=True
    )

    print("\n====== RANKED ELIGIBLE APPLICANTS ======")

    if not applicants:
        print("No eligible applicants found.")
    else:
        for rank, applicant in enumerate(applicants, start=1):
            print(
                rank, ".",
                applicant["name"],
                "| Course:", applicant["course"],
                "| Aggregate:", applicant["aggregate"], "%",
                "| Subject marks:", applicant["subject_mark"], "%"
            )

    print("\nTotal eligible applicants:", len(applicants))
    print("========================================")

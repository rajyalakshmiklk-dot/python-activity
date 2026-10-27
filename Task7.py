
# Student Performance Trend Analysis

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
exams = int(input("Enter number of examinations: "))

if students <= 0 or subjects <= 0 or exams < 2:
    print("Invalid input! Enter positive values and at least 2 exams.")

else:
    subject_names = []

    for i in range(subjects):
        name = input(f"Enter subject {i + 1} name: ")
        subject_names.append(name)

    for s in range(students):
        print("\n===== Student", s + 1, "=====")
        student_name = input("Enter student name: ")

        scores = []

        for e in range(exams):
            print("\nExamination", e + 1)
            exam_scores = []

            for subject in subject_names:
                while True:
                    try:
                        mark = float(input(f"Enter marks in {subject} (0-100): "))

                        if 0 <= mark <= 100:
                            exam_scores.append(mark)
                            break
                        else:
                            print("Marks must be between 0 and 100.")

                    except ValueError:
                        print("Please enter a valid number.")

            scores.append(exam_scores)

        # Calculate average percentage
        total_marks = sum(sum(exam) for exam in scores)
        maximum_marks = exams * subjects * 100
        average = (total_marks / maximum_marks) * 100

        # Compare first and last examinations
        improvements = []
        declines = []
        weak_subjects = []

        print("\n--- Performance Trend ---")

        for i, subject in enumerate(subject_names):
            change = scores[-1][i] - scores[0][i]

            print(subject, "change:", round(change, 2), "marks")

            if change > 0:
                improvements.append(subject)
            elif change < 0:
                declines.append(subject)

            # Weak in every examination: below 40
            if all(exam[i] < 40 for exam in scores):
                weak_subjects.append(subject)

        # Classification based on average
        if average >= 90:
            category = "Outstanding"
        elif average >= 75:
            category = "Very Good"
        elif average >= 60:
            category = "Good"
        elif average >= 40:
            category = "Needs Improvement"
        else:
            category = "At Risk"

        print("\n--- Student Report ---")
        print("Student Name:", student_name)
        print("Average Percentage:", round(average, 2), "%")
        print("Classification:", category)

        print("Improved Subjects:", improvements if improvements else "None")
        print("Declined Subjects:", declines if declines else "None")
        print("Consistently Weak Subjects:",
              weak_subjects if weak_subjects else "None")

        print("========================")

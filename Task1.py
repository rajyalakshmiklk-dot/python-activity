from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Subject:
    name: str
    marks: float
    maximum: float
    pass_mark: float


def validate_results(
    subjects: Sequence[Subject],
    grace_policy: str = "none",
    grace_limit: float = 0,
    classification_bands: Sequence[tuple[float, str]] = (
        (75, "Distinction"),
        (60, "First Class"),
        (50, "Second Class"),
        (40, "Pass"),
        (0, "Fail"),
    ),
) -> dict:
    """
    grace_policy:
      "none"       - do not award grace marks
      "per_subject" - award up to grace_limit to each subject, only enough to pass
      "total"      - award up to grace_limit across all subjects, only enough to pass

    Classification bands are (minimum percentage, label), highest first.
    """
    if grace_policy not in {"none", "per_subject", "total"}:
        raise ValueError("grace_policy must be 'none', 'per_subject', or 'total'")

    if grace_limit < 0:
        raise ValueError("grace_limit cannot be negative")

    if not subjects:
        raise ValueError("At least one subject is required")

    for subject in subjects:
        if subject.maximum <= 0:
            raise ValueError(f"{subject.name}: maximum must be greater than zero")
        if not 0 <= subject.pass_mark <= subject.maximum:
            raise ValueError(f"{subject.name}: pass mark must be between 0 and maximum")
        if not 0 <= subject.marks <= subject.maximum:
            raise ValueError(f"{subject.name}: marks must be between 0 and maximum")

    # Check whether the classification bands are sensibly ordered.
    if any(classification_bands[i][0] < classification_bands[i + 1][0]
           for i in range(len(classification_bands) - 1)):
        raise ValueError("Classification bands must be ordered highest to lowest")

    results = []
    grace_remaining = grace_limit

    for subject in subjects:
        awarded_grace = 0.0
        adjusted_marks = subject.marks

        if subject.marks < subject.pass_mark and grace_policy != "none":
            needed = subject.pass_mark - subject.marks
            available = grace_limit if grace_policy == "per_subject" else grace_remaining
            awarded_grace = min(needed, available, subject.maximum - subject.marks)
            adjusted_marks += awarded_grace

            if grace_policy == "total":
                grace_remaining -= awarded_grace

        passed = adjusted_marks >= subject.pass_mark
        results.append({
            "subject": subject.name,
            "original_marks": subject.marks,
            "grace_awarded": awarded_grace,
            "final_marks": min(adjusted_marks, subject.maximum),
            "maximum": subject.maximum,
            "pass_mark": subject.pass_mark,
            "status": "Pass" if passed else "Fail",
        })

    total_marks = sum(r["final_marks"] for r in results)
    total_maximum = sum(s.maximum for s in subjects)
    percentage = (total_marks / total_maximum) * 100
    overall_pass = all(r["status"] == "Pass" for r in results)

    classification = "Fail"
    if overall_pass:
        for threshold, label in classification_bands:
            if percentage >= threshold:
                classification = label
                break

    return {
        "subjects": results,
        "total_marks": total_marks,
        "total_maximum": total_maximum,
        "percentage": round(percentage, 2),
        "overall_status": "Pass" if overall_pass else "Fail",
        "classification": classification,
        "grace_policy": grace_policy,
        "grace_limit": grace_limit,
    }


if __name__ == "__main__":
    subjects = [
        Subject("Mathematics", marks=38, maximum=100, pass_mark=40),
        Subject("Science", marks=67, maximum=100, pass_mark=40),
        Subject("English", marks=72, maximum=100, pass_mark=40),
    ]

    result = validate_results(
        subjects,
        grace_policy="total",
        grace_limit=2,
    )

    for subject in result["subjects"]:
        print(
            f"{subject['subject']}: {subject['final_marks']}/{subject['maximum']} "
            f"(grace {subject['grace_awarded']}) — {subject['status']}"
        )

    print(
        f"\nTotal: {result['total_marks']}/{result['total_maximum']}"
        f"\nPercentage: {result['percentage']}%"
        f"\nOverall: {result['overall_status']}"
        f"\nClassification: {result['classification']}"
    )

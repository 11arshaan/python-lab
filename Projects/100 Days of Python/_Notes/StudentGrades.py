student_scores = {
    "1": 81,
    "2": 78,
    "3": 99,
    "4": 74,
    "5": 62
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    grade = ""
    if score >= 91:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    elif score < 71:
        grade = "Needs Improvement"
    student_grades[student] = grade

print(student_grades)

   

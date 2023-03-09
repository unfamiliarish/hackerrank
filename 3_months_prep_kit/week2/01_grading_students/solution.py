"""
    grades 0-100, inclusive
    grade < 40 is failing

    rounding:
    if (next mult of 5 - grade) < 3 
    then grade = next mult of 5

    if grade < 38, no rounding
"""


def round_grade(grade: int) -> int:
    if grade < 38:
        return grade

    # rounding grade
    grade_mod = grade % 5
    grade_diff = abs(grade_mod - 5)

    if grade_diff < 3:
        return grade + grade_diff

    return grade


def gradingStudents(grades: list[int]) -> list[int]:
    rounded_grades = [round_grade(grade) for grade in grades]
    return rounded_grades


assert round_grade(84) == 85
assert round_grade(29) == 29
assert round_grade(57) == 57


"""
    to 65
    64, 63 round
    else leave alone

    64 % 5 = 4
    63 % 5 = 3

    diffs:
    abs(4-5) = 1
    abs(3-5) = 2

    if diff < 3, then 
    round up, add diff to o.g. number
"""

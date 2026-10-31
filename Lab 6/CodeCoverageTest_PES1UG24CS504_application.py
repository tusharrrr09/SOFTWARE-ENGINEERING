
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


@pytest.mark.parametrize("marks, expected", [
    (95, "S"),
    (90, "S"),
    (85, "A"),
    (75, "B"),
    (65, "C"),
    (55, "D"),
    (45, "E"),
    (20, "F"),
    (0, "F"),
])
def test_letter_grade_valid(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_letter_grade_invalid(marks):
    with pytest.raises(ValueError):
        letter_grade(marks)


def test_final_marks_without_project():
    assert final_marks(30, 50, False) == 80


def test_final_marks_with_project():
    assert final_marks(30, 50, True) == 85


def test_final_marks_capped_at_100():
    assert final_marks(40, 60, True) == 100


def test_final_marks_internal_invalid():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)


def test_final_marks_external_invalid():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


def test_exam_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_exam_eligibility_attendance_75():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_eligibility_medical():
    assert exam_eligibility(65, True, True) == "eligible"


def test_exam_detained():
    assert exam_eligibility(60, True, False) == "detained"


import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


def test_letter_grade_boundaries():
    assert letter_grade(100) == "S"
    assert letter_grade(90) == "S"
    assert letter_grade(80) == "A"
    assert letter_grade(70) == "B"
    assert letter_grade(60) == "C"
    assert letter_grade(50) == "D"
    assert letter_grade(40) == "E"
    assert letter_grade(39) == "F"


def test_letter_grade_invalid_below_zero():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_letter_grade_invalid_above_hundred():
    with pytest.raises(ValueError):
        letter_grade(101)


def test_final_marks_valid_limits():
    assert final_marks(40, 60, False) == 100


def test_final_marks_project_below_limit():
    assert final_marks(30, 50, True) == 85


def test_final_marks_project_above_limit():
    assert final_marks(40, 60, True) == 100


def test_final_marks_internal_invalid():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)


def test_final_marks_external_invalid():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


def test_exam_fees_blocked():
    assert exam_eligibility(90, False, False) == "blocked"


def test_exam_attendance_eligible():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_medical_eligible():
    assert exam_eligibility(65, True, True) == "eligible"


def test_exam_medical_condition_false():
    assert exam_eligibility(70, True, False) == "detained"


def test_exam_attendance_below_medical_limit():
    assert exam_eligibility(60, True, True) == "detained"

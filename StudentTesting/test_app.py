from app import calculate_total
from app import calculate_grade
from app import check_result

# Test 1: Calculate total marks
def test_calculate_total():
    assert calculate_total([80, 75, 90]) == 245

# Test 2: Check grade
def test_calculate_grade():
    assert calculate_grade(95) == "A"

# Test 3: Check pass result
def test_check_pass():
    assert check_result(75) == "PASS"

# Test 4: Check fail result
def test_check_fail():
    assert check_result(35) == "FAIL"

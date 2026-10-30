from app import calculate_total


def test_calculate_total():
    assert calculate_total([80, 75, 90]) == 245


def test_empty_marks():
    assert calculate_total([]) == 0

def calculate_total(marks):
    return sum(marks)

def calculate_grade(total):
    if total >= 90:
        return "A"
    elif total >= 75:
        return "B"
    elif total >= 50:
        return "C"
    else:
        return "F"

def check_result(total):
    return "PASS" if total >= 50 else "FAIL"

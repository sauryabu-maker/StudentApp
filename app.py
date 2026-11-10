def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

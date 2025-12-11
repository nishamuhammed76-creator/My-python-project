def calculate_average(mark):
    """Accepts a list of marks and returns the average mark""")
    return sum(mark) / len(mark)

def calculate_average2(mark):
    """Accepts a list of marks and returns the average mark"""
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B+'
    elif average >= 60:
        return 'B'
    else:
        return 'C+'

def main():
    mark = [90, 80, 70, 60]
    print("Enter mark for Subjects")

    average = calculate_average(mark)
    average2 = calculate_average2(mark)

    print(average)
    print(average2)







    print(average)
    print(average2)


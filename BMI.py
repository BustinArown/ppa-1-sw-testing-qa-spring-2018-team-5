from math import isnan


# Calculates the bmi (Body Mass Index)
def bmi(feet, inch, weight):
    if not (isinstance(feet, float) and
            isinstance(inch, float) and
            isinstance(weight, float)):
        return float('NaN')

    inches = convert(feet, inch)
    b_mi = calculate_bmi(weight, inches)
    return determine(b_mi)


def convert(feet, inch):
    # Converts height in feet & inches to just inches
        return (feet * 12) + inch


def calculate_bmi(pounds, inches):
    try:
        return (pounds * 0.45) / ((inches * 0.025) ** 2)
    except ZeroDivisionError:
        print("Height cannot be zero")
        return float('NaN')


def determine(b_mi):
    if isnan(b_mi):
        return "Invalid input"
    if b_mi <= 18.5:
        return "Underweight"
    if 18.5 < b_mi <= 24.9:
        return "Normal weight"
    if 25 <= b_mi <= 29.9:
        return "Overweight"
    return "Obese"


def main():
    feet = int(input("Please input the foot of your height here: "))
    inch = int(input("Please input the inches of your height here: "))
    weight = int(input("Please input your weight here: "))

    # function call to calculate the bmi
    bmi(feet, inch, weight)


if __name__ == '__main__':
    main()

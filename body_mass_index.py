from math import isnan


# Calculates the bmi (Body Mass Index)
def body_mass_index(feet, inch, weight):
    inches = convert(feet, inch)
    b_mi = calculate_bmi(weight, inches)
    return determine(round(b_mi, 1))


def convert(feet, inch):
    # Converts height in feet & inches to just inches
    return (feet * 12) + inch


def calculate_bmi(pounds, inches):
    try:
        return (pounds * 0.45) / ((inches * 0.025) ** 2)
    except ZeroDivisionError:
        return float('NaN')


def determine(b_mi):
    if isnan(b_mi):
        return b_mi, "Height cannot be zero"
    if b_mi <= 18.5:
        return b_mi, "Underweight"
    if 18.5 < b_mi <= 24.9:
        return b_mi, "Normal weight"
    if 25 <= b_mi <= 29.9:
        return b_mi, "Overweight"
    return b_mi, "Obese"

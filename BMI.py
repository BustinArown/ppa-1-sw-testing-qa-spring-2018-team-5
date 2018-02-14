def bmi (feet, inch, weight):
    #Converts height in feet & inches to just inches
    inches = (feet * 12) + inch

    #Calculates the bmi (Body Mass Index)
    weightk = weight * 0.45
    heightm = inches * 0.025
    height2 = heightm * heightm
    b_mi = weightk / height2

    if (b_mi <= 18.5):
        print("Underweight")

    elif(b_mi > 18.5 and b_mi <= 24.9):
        print("Normal weight")

    elif (b_mi >= 25 and b_mi <= 29.9):
        print("Overweight")

    elif (b_mi > 30):
        print("Obese")


def main():
    feet = float(input("Please input the foot of your height here: "))
    inch = float(input("Please input the inches of your height here: "))
    weight = float(input("Please input your weight in pounds: "))

    bmi(feet, inch, weight)


main()


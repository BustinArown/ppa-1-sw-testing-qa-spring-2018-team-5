def bmi (feet, inch, weight):
    #calls the functiion that converts height into inches
    inches = convert(feet,inch)

    #Calculates the bmi (Body Mass Index)
    weightk = weight * 0.45
    heightm = inches * 0.025
    height2 = heightm * heightm
    b_mi = weightk / height2
    b_mi = int(b_mi)
    #calls the function that determines the weight category
    determine(b_mi)



def convert(feet, inch):
    # Converts height in feet & inches to just inches
        return (feet * 12) + inch

#function that determines weight category
def determine(b_mi):
    if (b_mi <= 18.5):
        print("Underweight")
        b_mi = "Underweight"

    elif (b_mi > 18.5 and b_mi <= 24.9):
        print("Normal weight")
        b_mi = "Normal weight"

    elif (b_mi >= 25 and b_mi <= 29.9):
        print("Overweight")
        b_mi = "Overweight"

    elif (b_mi > 30):
        print("Obese")
        b_mi = "Obese"

    return b_mi


def main():
    #Error handling for non number inputs
    incorrect = True
    while (incorrect):
        try:

            feet = int(input("Please input the foot of your height here: "))


        except ValueError:
            print ("Please enter a number")

        else:
            incorrect = False

    incorrect = True
    while (incorrect):
        try:

            inch = int(input("Please input the inches of your height here: "))


        except ValueError:
            print ("Please enter a number")

        else:
            incorrect = False

    incorrect = True
    while (incorrect):
        try:

            weight = int(input("Please input your weight here: "))


        except ValueError:
            print ("Please enter a number")

        else:
            incorrect = False


    #function call to calculate the bmi
    bmi(feet, inch, weight)


if __name__ == '__main__':

    main()


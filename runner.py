import body_mass_index
import retirement
import shortest_distance
import email_verifier
import split_the_tip
import math


def print_prompt():
    print("You may choose from any 5 functions:\n"
          "1-Body Mass Index Calculator\n"
          "2-Retirement Goal Determiner\n"
          "3-Distance Formula Calculator\n"
          "4-Email Address Verifier\n"
          "5-Tip splitter\n\n"
          "Which function do you want?")


def get_function_number():
    print_prompt()
    while True:
        value = input("Enter any number from 1 to 5. R to repeat, X to exit. ")
        value = value.lower()
        if value == "r":
            print_prompt()
        elif value == "x":
            return 0
        else:
            try:
                value = int(value)
            except ValueError:
                value = int(0)
            if 0 <= value <= 5:
                return value
            print("Invalid function input")
            continue


def get_body_mass_index_args():
    while True:
        print("What is the height in feet and inches and weight in pounds? x to exit")
        num_feet = input("Feet: ")
        if num_feet.lower() == "x":
            return int("NaN"), int("NaN"), int("NaN")
        try:
            num_feet = int(num_feet)
            num_inches = int(input("Inches: "))
            break
        except ValueError:
            print("Must be an integer")
            continue

    while True:
        try:
            num_weight = int(input("Pounds? "))
            return num_feet, num_inches, num_weight
        except ValueError:
            print("Must be a number")
            continue


def get_retirement_args():
    while True:
        print("What is the current age, salary, percentage saved, and goal? x to exit")
        current_age = input("Age: ")
        if current_age.lower() == "x":
            return float("NaN"), float("NaN"), float("NaN"), float("NaN")
        try:
            current_age = int(current_age)
            if not (0 <= current_age <= 99):
                print("Age must be between 0 and 100")
                continue
            income = int(input("Salary: "))
            if income < 0:
                print("Salary must be positive")
                continue
            save_percentage = int(input("Percentage of income saved: "))
            if not (0 < save_percentage <= 100):
                print("Percentage saved must be between 1 and 100")
                continue
            goal_amount = int(input("Desired amount of money: "))
            if goal_amount < 0:
                print("Goal amount must be positive")
                continue
        except ValueError:
            print("Must be an integer")
            continue

        return current_age, income, save_percentage, goal_amount


def get_shortest_distance_args():
    while True:
        print("What are the two points (x1,y1) and (x2,y2)? x to exit")
        x1 = input("x1: ")
        if x1.lower() == "x":
            return float("NaN"), float("NaN"), float("NaN"), float("NaN")
        try:
            x1 = float(x1)
            y1 = float(input("y1: "))
            x2 = float(input("x2: "))
            y2 = float(input("y2: "))
        except ValueError:
            print("Must be a number")
            continue
        return x1, y1, x2, y2


def get_split_the_tip_args():
    while True:
        print("What is the bill and the number of people? x to exit")
        amount = input("Bill: ")
        if amount.lower() == "x":
            return float("NaN"), float("NaN")
        try:
            amount = float(amount)
            if amount < 0:
                print("Bill must be positive")
                continue
            num_guests = int(input("Guests: "))
            if num_guests < 0:
                print("Must be a non-negative integer")
                continue
        except ValueError:
            print("Must be integers")
            continue
        return amount, num_guests


if __name__ == "__main__":
    print("Welcome to assignment 1")
    while True:
        function_choice = get_function_number()
        if function_choice == 0:
            break

        if function_choice == 1:
            feet, inches, weight = get_body_mass_index_args()
            if math.isnan(feet):
                continue
            bmi, category = body_mass_index.body_mass_index(feet, inches, weight)
            if math.isnan(bmi):
                print(category)
            else:
                print("Results in a bmi of %f. %s" % (bmi, category))

        elif function_choice == 2:
            age, salary, saved, goal = get_retirement_args()
            if math.isnan(age):
                continue
            retirement_age = retirement.retirement(age, salary, saved, goal)
            if retirement_age == -1:
                print("Will not meet goal")
            else:
                print("Will meet goal at %d" % retirement_age)

        elif function_choice == 3:
            x1, y1, x2, y2 = get_shortest_distance_args()
            if math.isnan(x1):
                continue
            print("The distance between (%f,%f) and (%f,%f) is %f." % (x1, y1,
                                                                       x2, y2,
                                                                       shortest_distance.shortest_distance(x1, y1, x2, y2)))

        elif function_choice == 4:
            address = input("Enter a email address to validate. x to exit ")
            if address == "x":
                continue
            if email_verifier.email_verifier(address):
                print("%s is a valid email." % address)
            else:
                print("%s is an invalid email." % address)

        else:
            amount, num_guests = get_split_the_tip_args()
            if math.isnan(amount):
                continue
            print("The tip splits to")
            print(split_the_tip.split_the_tip(amount, num_guests))
        print("\n\n")
        continue

    print("Thank you for using assignment 1 functions")

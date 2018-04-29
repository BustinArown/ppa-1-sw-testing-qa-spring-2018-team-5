#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import math

input_data=cgi.FieldStorage()

def retirement(age, salary, percentage_saved, desired_amount):
    amount_saved_per_year = salary * percentage_saved / 100 * 1.35
    years_to_achieve = math.ceil(desired_amount / amount_saved_per_year)
    if (years_to_achieve + age >= 100):
        return -1
    return age + years_to_achieve


def main():  
    print ("Content-type: text/html")
    print ("")
    print ("<html><head>")
    print ("</head>")
    print ("<body>")
    try:
        current_age = int(input_data["age"].value)
        if not (0 <= current_age <= 99):
            print ("Age must be between 0 and 100")
            return

        income = int(input_data["sal"].value)
        if (income < 0):
            print ("Salary must be positive")
            return

        save_percentage = float(input_data["save"].value)
        if not (0 < save_percentage <= 100):
            print ("Percentage saved must be between 1 and 100")
            return

        goal_amount = float(input_data["goal"].value)
        if (goal_amount < 0):
            print ("Goal amount must be positive")
            return
    
    except ValueError:
        print ("Must be an integer")
        return
    retirement_age = retirement(current_age, income, save_percentage, goal_amount)
    print ("<h3>")
    if (retirement_age == -1):
        print ("Will not meet goal")
    else:
        print ("Will meet goal at ", retirement_age)
    print ("</h3>")
    
    print ("</body></html>")
    	
    
if __name__ == '__main__':
    main()
 


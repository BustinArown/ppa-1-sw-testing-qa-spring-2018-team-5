#
# Retirement- Input user's current age, annual salary, percentage saved (employer matches 35% of
# savings). Input desired retirement savings goal. Output what age savings goal will be met. You can
# assume death at 100 years (therefore, indicate if the savings goal is not met).
def main():
    print("Welcome to the Retirement Savings Calculator")
    curr_age = int(input("How old are you currently? "))
    salary = int(input("What is your annual salary? "))
    saved = int(input("What percentage have you saved? "))
    desired = int(input("What is your desired retirement savings? "))

    inc_age = curr_age
    curr_saved = (salary * (saved / 100))
    employer = (curr_saved * (35 / 100))
    ##following line for testing only
    return curr_saved
    while inc_age <= 100:
        if inc_age == 100:
            print("Sorry, you missed your goal.")
            break
        if curr_saved >= desired:
            print("You will meet your savings goal at", inc_age)
            break
        else:
            curr_saved += employer
            inc_age += 1


if __name__ == '__main__':
    main()

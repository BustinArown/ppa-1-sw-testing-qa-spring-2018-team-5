import math


def retirement(age, salary, percentage_saved, desired_amount):
    amount_saved_per_year = salary * percentage_saved / 100 * 1.35
    years_to_achieve = math.ceil(desired_amount / amount_saved_per_year)
    if years_to_achieve + age >= 100:
        return -1
    return age + years_to_achieve

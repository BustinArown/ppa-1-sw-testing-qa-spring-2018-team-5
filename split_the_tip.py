import math


def split_the_tip(total, guest_number):
    total += total * 0.15  # Calculate and add gratuity with the total amount
    total = round(total * 100) / 100  # Make total round upto 2 decimal points

    tip = math.floor(total * 100 / guest_number) / 100  # Compute the minimum amount given by each guest
    split_tips = [tip] * guest_number  # This list contains the tips for all guests

    # Compute the remaining tip that need to be equally distributed among the guests
    remaining = round(total - tip * guest_number, 2)

    if remaining > 0.0:
        extra = remaining / .01  # number of guests who will pay the remaining amount
        for k in range(int(round(extra))):
            split_tips[k] += 0.01  # Distribute the remaining amount to the guests from the beginning of the list
            split_tips[k] = round(split_tips[k], 2)
    return split_tips

import re


def is_valid_email(address):
    double_period_ex = re.compile('[.][.]')
    if double_period_ex.search(address) is not None:
        return False
    regex = re.compile('[a-z][a-z0-9!$%^*+-={|}._?~]*[@][a-z0-9!$%^*+-={|}_?~]+[.][a-z0-9!$%^*+-={|}_?~]+', re.IGNORECASE)
    return regex.match(address) is not None

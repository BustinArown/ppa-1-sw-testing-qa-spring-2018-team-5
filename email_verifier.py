import re


def is_valid_email(address):
    double_period_ex = re.compile('[.][.]')
    regex = re.compile('[a-z][a-z0-9!$%^*+-={|}._?~]*[@][a-z0-9!$%^*+-={|}_?~]+[.][a-z0-9!$%^*+-={|}_?~]+', re.IGNORECASE)
    return double_period_ex.search(address) is None and regex.match(address) is not None

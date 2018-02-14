import re


def is_valid_email(address):
    regex = re.compile('[a-zA-Z][[.]?\w+]*@\w')
    return regex.match(address) is not None

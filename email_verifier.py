import re


def is_valid_email(address):
    regex = re.compile('[\D]+@')
    return regex.match(address) is not None

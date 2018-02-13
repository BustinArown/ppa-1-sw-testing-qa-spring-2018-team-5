import re


def is_valid_email(address):
    regex = re.compile('[\w]+@')
    return regex.match(address) is not None

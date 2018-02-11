import re


def is_valid_email(address):
    regex = re.compile('[\w]+@')
    if regex.match(address) is None:
        return False
    return True

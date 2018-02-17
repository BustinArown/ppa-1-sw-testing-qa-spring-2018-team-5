import re

def is_valid_email(address):
    return re.compile('[.][.]').search(str(address)) is None and \
            re.compile('[a-z][a-z0-9!$%^*+-={|}._?~]*[@][a-z0-9!$%^*+-={|}_?~]+[.][a-z0-9!$%^*+-={|}_?~]+', re.IGNORECASE).match(str(address)) is not None

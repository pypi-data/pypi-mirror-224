import re

def validate_name(name: str) -> bool:
    """
    Validate the names.

    :param name: str -> The name to be validated as a string
    :return: True if the name is valid, False otherwise.

    """
    if re.match(r'^\b(?<!-)([\s\-’]{0,1}\w(?!_))+(?!-)\b(?:\.)?(?:\s)?$', name):
        return True
    return False

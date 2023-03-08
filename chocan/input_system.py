MAX_NAME = 25
MAX_CITY = 14
MAX_STATE = 2
MIN_ZIP = 10000
MAX_ZIP = 99999
MIN_USER_NUMBER = 1
MAX_USER_NUMBER = 999999999

def get_input(max : int) -> str:
    """
    Strips the input's leading and trailing whitespace and returns the
    the first 'max' chars of the stripped input, with the first letter
    capitalized.
    """
    if max < 0:
        raise ValueError('max must be a non-negative integer')
    user_input = input()
    nice_input = user_input.strip().capitalize()
    return nice_input[0:max]
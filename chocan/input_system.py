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
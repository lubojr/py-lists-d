def pets_begin_letter(pets, letter):
    """
    a function that returns pets in a list
    (list given as the argument) that begin with a letter case insensitive.

    Args:
        pets (list): list of pets to search in
        letter (string): letter to check if beginning on

    Returns:
        list: results
    """
    results = []
    if isinstance(letter, str):
        for name in pets:
            if isinstance(name, str):
                if name.lower().startswith(letter.lower()):
                    results.append(name)
    return results

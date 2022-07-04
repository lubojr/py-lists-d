def pets_begin_d(pets):
    """
    a function that returns pets in a list
    (list given as the argument) that begin with a 'd'.

    Args:
        pets (list): list of pets to search in

    Returns:
        list: list of pets
    """
    res = []
    for name in pets:
        if name[0] == 'd':
            res.append(name)
    return res

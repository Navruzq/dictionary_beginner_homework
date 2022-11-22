def find_max_key(data: dict) -> int:
    """
    Return the maximum key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    a = 0
    for i in data.keys():
        if a<i:
            a=i
    return a

print(find_max_key({1:'a', 2:'b', 3: 'c'}))
def get_country_with_least_users(data:list) -> str:
    """
    Return the country with the least users

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The country with the least users
    """
    a=data[0]['country']
    b=data[1]['country']
    if len(a)>len(b):
        return b
    else:
        return a
    
print(get_country_with_least_users([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]))
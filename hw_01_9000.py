# Homework 9000
# Author: Chris Proctor


def list_add(values0, values1):
    """
    Performs a bunch of additions at once, adding each element in `values0` to the
    corresponding element in `values1`. `values0` and `values1` must be the same length,
    which will be the same length as the returned list.

        >>> list_add([1, 2, 3], [2, 2, 2])
        [3, 4, 5]
    """
    return []

def list_subtract(values0, values1):
    """
    Performs a bunch of subtractions at once, subtracting each element in `values1` from the
    corresponding element in `values0`. `values0` and `values1` must be the same length,
    which will be the same length as the returned list.

        >>> list_subtract([1, 2, 3], [3, 2, 1])
        [-2, 0, 2]
    """
    return []

def list_max(values0, values1):
    """
    Returns the elementwise max of two lists. For each pair of items from `values0`
    and `values1`, the larger is in the result list.

        >>> list_max([1, 2, 3, 4], [5, 4, 3, 2])
        [5, 4, 3, 4]
    """
    return []

def dict_merge(dict0, dict1):
    """
    Takes two dictionaries of string-string key-value pairs and merges them into a single dictionary
    with each key-value pair. If a key exists in both dictionaries, the function appends the value
    from dict2 to the value from dict1 with a space inbetween and associates the new value with the key.

        >>> merge_dict({'red': 'rojo', 'blue': 'azul'}, {'purple': '紫色', 'blue': '蓝色'})
        {'red': 'rojo', 'blue': 'azul 蓝色', 'purple': '紫色'}
    """

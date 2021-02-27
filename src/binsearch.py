"""
Binary search
"""


def binary_search0(xs, x):
    """
    Perform binary search for a specific value in the given sorted list

    :param xs: a sorted list
    :param x: the target value
    :return: an index if the value was found, or None if not
    """
    lft, rgt = 0, len(xs) - 1

    while lft <= rgt:
        mid = (lft + rgt) // 2
        if xs[mid] == x:
            return mid
        if xs[mid] < x:
            lft = mid + 1
        else:
            rgt = mid - 1

    return None


def binary_search1(xs, x):
    """
    Perform binary search for a specific value in the given sorted list

    :param xs: a sorted list
    :param x: the target value
    :return: an index if the value was found, or None if not
    """
    lft, rgt = 0, len(xs)

    while lft < rgt:
        mid = (lft + rgt) // 2
        if xs[mid] == x:
            return mid
        if xs[mid] < x:
            lft = mid + 1
        else:
            rgt = mid

    return None

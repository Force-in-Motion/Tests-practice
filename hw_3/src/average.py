def average(lst):
    if not isinstance(lst, list):
        raise TypeError()
    if len(lst) == 0:
        raise ValueError()
    return sum(lst) / len(lst)
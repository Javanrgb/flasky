print("Imported my_modules")

test = "Test String"


def find_index(to_search, target):
    """finds index of a value"""
    for i, value in enumerate(to_search):
        if value == target: return i

    return -1

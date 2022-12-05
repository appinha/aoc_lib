def get_min_value_key(dictionary):
    return min(dictionary, key=dictionary.get)


def get_max_value_key(dictionary):
    return max(dictionary, key=dictionary.get)

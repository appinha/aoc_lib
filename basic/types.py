def is_int(object: object):
    return (isinstance(object, int))


def is_float(object: object):
    return (isinstance(object, float))


def is_number(object: object):
    return is_int(object) or is_float(object)


def is_str(object: object):
    return (isinstance(object, str))


def is_list(object: object):
    return (isinstance(object, list))


def is_dict(object: object):
    return (isinstance(object, dict))


def str_to_int(s: str):
    if is_str(s) and s.isdigit():
        return int(s)
    else:
        return s

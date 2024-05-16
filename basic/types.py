from __future__ import annotations
from typing import Any, TypeVar
from typing_extensions import Protocol


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool: ...

    def __lt__(self: C, other: C) -> bool: ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


C = TypeVar("C", bound="Comparable")
T = TypeVar("T")


def is_int(object: object):
    return isinstance(object, int)


def is_float(object: object):
    return isinstance(object, float)


def is_number(object: object):
    return is_int(object) or is_float(object)


def is_str(object: object):
    return isinstance(object, str)


def is_list(object: object):
    return isinstance(object, list)


def is_dict(object: object):
    return isinstance(object, dict)


def str_to_int(s: str):
    if is_str(s) and s.isdigit():
        return int(s)
    else:
        return s


def list_to_str(lst: list):
    return "".join(lst)

import collections
import itertools
from typing import Iterable


def cycle(iterable: Iterable):
    return itertools.cycle(iterable)


def count_occurrences(iterable: Iterable):
    """Returns a dict with occurrence count by item.
    Example:
        count_occurrences([1, 1, 1, 2, 2, 3, 1, 2]) -> {1: 4, 2: 3, 3: 1}"""
    return collections.Counter(iterable)


def count_sequenced_occurrences(iterable: Iterable):
    """Returns a list with occurrence count by item.
    Example:
        count_occurrences([1, 1, 1, 2, 2, 1, 1, 2]) -> [{item: 1, occurrences: 3},
        {item: 2, occurrences: 2}, {item: 1, occurrences: 2}, {item: 2, occurrences: 1}]"""
    return [{"item": k, "occurrences": len(list(v))} for k, v in itertools.groupby(iterable)]


def flatten_list(list2D):
    return list(itertools.chain(*list2D))


def list_combinations(iterable: Iterable, n: int):
    """Returns a list with combinations of given number of elements.

    Example:
        list_combinations([0, 1, 2, 3], 2) -> [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]"""
    return list(itertools.combinations(iterable, n))


def list_sequenced_subsets(iterable: Iterable, n: int):
    """Returns a list of sequenced subsets of given number of elements.

    Example:
        list_sequenced_subsets([0, 1, 2, 3], 2) -> [[0, 1], [1, 2], [2, 3]]"""
    return [iterable[i : i + n] for i in range(len(iterable) - (n - 1))]


def list_unique_permutations(elements: Iterable, include_reversed=False):
    if not include_reversed:
        return list(set(itertools.permutations(elements)))

    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations

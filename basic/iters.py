import itertools
import typing as t


def cycle(iterable: t.Iterable):
    return itertools.cycle(iterable)

def count_sequenced_occurrences(iterable: t.Iterable):
    return [
        {"item": k, "occurrences": len(list(v))}
        for k, v in itertools.groupby(iterable)
    ]

def flatten_list(list2D):
    return list(itertools.chain(*list2D))


def list_combinations(iterable: t.Iterable, n: int):
    '''Returns a list with combinations of given number of elements.

    Example:
        list_combinations([0, 1, 2, 3], 2) -> [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]'''
    return list(itertools.combinations(iterable, n))


def list_sequenced_subsets(iterable: t.Iterable, n: int):
    '''Returns a list of sequenced subsets of given number of elements.

    Example:
        list_sequenced_subsets([0, 1, 2, 3], 2) -> [[0, 1], [1, 2], [2, 3]]'''
    return [set[i:i + n] for i in range(len(set) - (n - 1))]


def list_unique_permutations(elements: t.Iterable):
    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations

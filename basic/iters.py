import itertools
import typing as t


def cycle(iterable: t.Iterable):
    return itertools.cycle(iterable)

def count_occurrences(iterable: t.Iterable):
    return [
        {"item": k, "occurrences": len(list(v))}
        for k, v in itertools.groupby(iterable)
    ]


def list_combinations(iterable: t.Iterable, n: int):
    return list(itertools.combinations(iterable, n))


def list_unique_permutations(elements: t.Iterable):
    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations

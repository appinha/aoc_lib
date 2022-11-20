import itertools


def count_occurrences(iterable):
    return [
        {"item": k, "occurrences": len(list(v))}
        for k, v in itertools.groupby(iterable)
    ]


def list_combinations(iterable, n):
    return list(itertools.combinations(iterable, n))


def list_unique_permutations(elements):
    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations

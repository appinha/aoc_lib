import itertools


def count_occurrences(iterator):
    return [
        {"item": k, "occurrences": len(list(v))}
        for k, v in itertools.groupby(iterator)
    ]

def get_unique_permutations(elements):
    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations

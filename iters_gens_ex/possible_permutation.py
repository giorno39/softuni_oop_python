import itertools

def possible_permutations(seq):
    permutations = list(itertools.permutations(seq))
    for per in permutations:
        yield list(per)


[print(n) for n in possible_permutations([1, 2, 3])]


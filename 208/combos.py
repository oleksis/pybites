from itertools import combinations

def find_number_pairs(numbers, N=10):
    comb = combinations(numbers, 2)
    return [c for c in comb if c[0] + c[1] == N]

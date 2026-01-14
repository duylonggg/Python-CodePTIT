from itertools import combinations

n, k = map(int, input().split())
a = sorted(set(map(int, input().split())))

for comb in combinations(a, k):
    print(*comb)

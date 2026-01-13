import math

t = int(input())
for _ in range(t):
    N, X, M = map(float, input().split())
    r = X / 100.0

    years = math.log(M / N) / math.log(1 + r)
    years = math.ceil(years)

    print(years)

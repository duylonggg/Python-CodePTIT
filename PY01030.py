import math

N, K = map(int, input().split())
min = 10 ** (K - 1)
max = 10 ** K - 1
for i in range(min, max + 1):
    if math.gcd(i, N) == 1:
        print(i, end=' ')
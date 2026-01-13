t = int(input())
for _ in range(t):
    N = int(input())
    m = 10
    while m <= 1_000_000_000:
        if N < m:
            break
        N = ((N + m // 2) // m) * m
        m *= 10
    print(N)

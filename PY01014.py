a, K, N = map(int, input().split())

maxB = N - a
if maxB <= 0:
    print(-1)
else:
    b0 = (K - a % K) % K
    if b0 == 0:
        b0 = K

    if b0 > maxB:
        print(-1)
    else:
        res = list(range(b0, maxB + 1, K))
        print(' '.join(map(str, res)))

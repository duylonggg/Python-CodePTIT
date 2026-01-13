t = int(input())
for _ in range(t):
    n = int(input())
    res = ["1"]

    p = 2
    while p * p <= n:
        cnt = 0
        while n % p == 0:
            cnt += 1
            n //= p
        if cnt:
            res.append(f"{p}^{cnt}")
        p += 1

    if n > 1:
        res.append(f"{n}^1")

    print(" * ".join(res))

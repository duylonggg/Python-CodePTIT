import sys
from math import gcd

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out = []

    INF = 10**30

    for _ in range(T):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        c = [int(next(it)) for _ in range(n)]

        dp = {}

        for ai, ci in zip(a, c):
            ndp = dict(dp)
            prev = ndp.get(ai, INF)
            if ci < prev:
                ndp[ai] = ci

            for g, cost in dp.items():
                ng = gcd(g, ai)
                cand = cost + ci
                prev = ndp.get(ng, INF)
                if cand < prev:
                    ndp[ng] = cand

            dp = ndp

        out.append(str(dp.get(1, -1)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

import sys

data = sys.stdin.read().strip().split()
t = int(data[0])
idx = 1

for _ in range(t):
    N = int(data[idx]); idx += 1
    start = 2 if N % 2 == 0 else 1

    s = 0.0
    for i in range(start, N + 1, 2):
        s += 1.0 / i

    print(f"{s:.6f}")

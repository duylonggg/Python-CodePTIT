import math

t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if math.gcd(n, int(str(n)[::-1])) == 1 else "NO")
import math

t = int(input())
for _ in range(t):
    n = int(input())
    k = 0

    for i in range(1, n):
        if math.gcd(i, n) == 1:
            k += 1

    def is_prime(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False

        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 and n % (i + 2) == 0:
                return False
        return True

    print("YES" if is_prime(k) else "NO")
import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    gcd = math.gcd(a, b)

    total = sum(int(num) for num in str(gcd))

    def is_prime(n):
        if n < 2: return False
        if n < 4: return True
        if n % 2 == 0 or n % 3 == 0: return False

        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    print("YES" if is_prime(total) else "NO")
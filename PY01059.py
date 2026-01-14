from math import prod

t = int(input())
for _ in range(t):
    s = input().strip()

    even_sum = sum(int(s[i]) for i in range(0, len(s), 2))

    odd_digits = [int(s[i]) for i in range(1, len(s), 2) if s[i] != '0']
    odd_prod = prod(odd_digits) if odd_digits else 0

    print(even_sum, odd_prod)

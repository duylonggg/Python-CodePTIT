from math import prod

t = int(input())
for _ in range(t):
    s = input().strip()

    odd_sum = sum(int(s[i]) for i in range(1, len(s), 2))

    even_digits = [int(s[i]) for i in range(0, len(s), 2) if s[i] != '0']
    even_prod = prod(even_digits) if even_digits else 0

    print(even_prod, odd_sum)

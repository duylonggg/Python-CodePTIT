from math import prod

for _ in range(int(input())):
    print(prod(int(c) for c in input().strip() if c != '0'))

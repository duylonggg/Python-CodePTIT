t = int(input())
for _ in range(t):
    s = input()

    n = sum(int(c) for c in s)
    print("YES" if n == int(str(n)[::-1]) and n > 9 else "NO")
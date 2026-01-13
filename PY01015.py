t = int(input())
for _ in range(t):
    s = input()
    print("YES" if s == "".join(sorted(s)) else "NO")
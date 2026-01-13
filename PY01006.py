t = int(input())
for _ in range(t):
    s = input()
    print("YES" if s.count('4') + s.count('7') == len(s) else "NO")

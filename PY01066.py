import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()
    r = s[::-1]

    ok = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            ok = False
            break

    print("YES" if ok else "NO")

t = int(input())
for _ in range(t):
    s = input().strip()

    if len(set(s)) != 2:
        print("NO")
        continue

    ok = True
    for i in range(len(s) - 2):
        if s[i] != s[i + 2]:
            ok = False
            break

    print("YES" if ok else "NO")

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)

    if n < 3:
        print("NO")
        continue

    peak = -1
    for i in range(1, n - 1):
        if s[i - 1] < s[i] > s[i + 1]:
            peak = i
            break

    if peak == -1:
        print("NO")
        continue

    ok = True

    for i in range(peak):
        if s[i] >= s[i + 1]:
            ok = False
            break

    for i in range(peak, n - 1):
        if s[i] <= s[i + 1]:
            ok = False
            break

    print("YES" if ok else "NO")

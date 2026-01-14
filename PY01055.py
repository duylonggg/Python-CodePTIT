for _ in range(int(input())):
    s = input()
    print("YES" if len(s) & 1 and s[0] != s[1] and (s[i] == s[i + 2] for i in range(1, len(s), 2)) else "NO")
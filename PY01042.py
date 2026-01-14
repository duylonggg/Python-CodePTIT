t = int(input())
for _ in range(t):
    s = input()

    print("YES" if sum(c == '0' or c == '1' or c == '2' for c in s) == len(s) else "NO")
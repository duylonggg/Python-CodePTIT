t = int(input())
for _ in range(t):
    s = input().strip()
    first2 = s[:2]
    last2 = s[-2:]
    print("YES" if first2 == last2 else "NO")
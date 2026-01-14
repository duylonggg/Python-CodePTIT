for _ in range(int(input())):
    print("YES" if sum(int(c) for c in input()) % 3 == 0 else "NO")
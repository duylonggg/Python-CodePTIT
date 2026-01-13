def mod10(n):
    return sum(int(num) for num in str(n)) % 10 == 0

def diff2(n):
    s = str(n)
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != 2:
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("YES" if mod10(n) and diff2(n) else "NO")

main()

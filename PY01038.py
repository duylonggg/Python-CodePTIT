t = int(input())
for _ in range(t):
    n = int(input())

    def check(n):
        for _ in range(1000):
            if n % 7 == 0:
                return n
            n += int(str(n)[::-1])
        return -1

    print(check(n))
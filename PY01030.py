import math

N, K = map(int, input().split())
start = 10 ** (K - 1)
end = 10 ** K - 1

cnt = 0
for i in range(start, end + 1):
    if math.gcd(i, N) == 1:
        print(i, end=' ')
        cnt += 1
        if cnt % 10 == 0:
            print()  # xuống dòng sau mỗi 10 số

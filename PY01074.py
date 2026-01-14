import sys

def linear_sieve_spf(n: int):
    spf = [0] * (n + 1)
    primes = []
    spf[1] = 1
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            v = i * p
            if v > n:
                break
            spf[v] = p
            if p == spf[i]:
                break
    return spf

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    arr = data[1:1 + t]
    if not arr:
        print(0)
        return

    maxA = max(arr)

    spf = linear_sieve_spf(maxA)

    # sum_pf[x] = tổng các thừa số nguyên tố của x (tính cả bội số)
    sum_pf = [0] * (maxA + 1)
    for x in range(2, maxA + 1):
        p = spf[x]
        sum_pf[x] = sum_pf[x // p] + p

    total = 0
    for x in arr:
        total += sum_pf[x]

    sys.stdout.write(str(total))

if __name__ == "__main__":
    main()

def gen_pal():
    digits = ['0', '2', '4', '6', '8']
    first = ['2', '4', '6', '8']
    res = []

    # Độ dài 2: ab -> abba dạng rút gọn chỉ là aa
    for a in first:
        s = int(a + a)
        res.append(s)

    # Độ dài 4: ab|ba
    for a in first:
        for b in digits:
            s = int(a + b + b + a)
            res.append(s)

    # Độ dài 6: abc|cba
    for a in first:
        for b in digits:
            for c in digits:
                s = int(a + b + c + c + b + a)
                if s < 1_000_000:
                    res.append(s)

    res.sort()
    return res


all_nums = gen_pal()

t = int(input())
for _ in range(t):
    N = int(input())
    ans = [str(x) for x in all_nums if x < N]
    print(" ".join(ans))

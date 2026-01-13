t = int(input())
for _ in range(t):
    s = input()
    encode = ""

    cur = s[0]
    time = 0
    for chr in s[1:]:
        if chr == cur:
            time += 1
        else:
            encode += str(time + 1) + cur
            cur = chr
            time = 0
    print(encode + str(time + 1) + cur)
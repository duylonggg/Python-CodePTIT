P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    s = input()
    if int(s[0]) == 0:
        break
    K, S = s.split()
    K = int(K)
    enc = ''.join(P[(P.index(c) + K) % 28] for c in S)
    print(enc[::-1])

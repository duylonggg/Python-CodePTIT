import sys

def gen(L):
    s = [''] * L
    out = []
    def dfs(i, a, b, c):
        if i == L:
            if a > 0 and b > 0 and c > 0 and a <= b <= c:
                out.append(''.join(s))
            return

        s[i] = 'A'
        dfs(i + 1, a + 1, b, c)

        s[i] = 'B'
        dfs(i + 1, a, b + 1, c)

        s[i] = 'C'
        dfs(i + 1, a, b, c + 1)

    dfs(0, 0, 0, 0)
    return out

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    N = int(data)

    res = []
    for L in range(3, N + 1):
        res.extend(gen(L))

    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()

def hanoi(n, src, aux, dst):
    if n == 1:
        print(f"{src} -> {dst}")
        return
    hanoi(n - 1, src, dst, aux)
    print(f"{src} -> {dst}")
    hanoi(n - 1, aux, src, dst)

n = int(input().strip())
hanoi(n, 'A', 'B', 'C')

import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1+n]

    st = []
    for x in a:
        if st and ((st[-1] ^ x) & 1) == 0:
            st.pop()
        else:
            st.append(x)

    print(len(st))

if __name__ == "__main__":
    main()

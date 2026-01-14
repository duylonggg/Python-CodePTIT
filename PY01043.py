first = ['2', '4', '6', '8']
digit = ['0', '2', '4', '6', '8']
nums = []

for a in first:
    nums.append(int(a + a))

for a in first:
    for b in digit:
        nums.append(int(a + b + b + a))

for a in first:
    for b in digit:
        for c in digit:
            nums.append(int(a + b + c + c + b + a))

nums.sort()

t = int(input())
for _ in range(t):
    n = int(input())
    for num in nums:
        if num < n:
            print(num, end=' ')
        else:
            break
    print()

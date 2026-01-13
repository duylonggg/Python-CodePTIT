s = input()
low = sum(c.islower() for c in s)
upp = len(s) - low

print(s.lower() if low >= upp else s.upper())

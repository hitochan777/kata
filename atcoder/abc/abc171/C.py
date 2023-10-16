n = int(input())
n -= 1
s = []
while n >= 0:
    s.append(chr(ord("a") + (n % 26)))
    n = n // 26 - 1

print("".join(s)[::-1])


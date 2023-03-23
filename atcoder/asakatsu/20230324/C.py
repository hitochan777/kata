n, m = (int(x) for x in input().split())
n %= 12
na = 360 * (n / 12) + (m / 60) * (360 / 12)
ma = 360 * (m / 60)
# print(na, ma)
d = abs(na - ma)
print(min(360 - d, d))
x, y, a, b = list(map(int, input().split()))

exp = 0
while x < min(b / a, y - 1):
    x *= a
    exp += 1

exp += max(0, y - x - 1) // b
print(exp)
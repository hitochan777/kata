import math
X, Y, R = list(map(lambda x: int(float(x) * 10000), input().split()))

cnt = 0
for x in range((X - R) // 10000, (X + R) // 10000 + 1):
    diff = R ** 2 - (x * 10000 - X) ** 2
    if diff < 0:
        continue

    h = math.sqrt(diff)
    cnt += int(((Y + h) // 10000) - ((Y - h  - 1) // 10000))

print(cnt)
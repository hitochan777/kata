sx, sy, gx, gy = list(map(int, input().split()))
gy = -gy
print(1 - sy * (gx - sx) / (gy - sy))
print(gx - sx)
print(gy - sy)
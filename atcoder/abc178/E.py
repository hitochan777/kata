max_z = 0 
min_z = 10**10
max_w = -10**10
min_w = 10**10
N = int(input())
for _ in range(N):
    x, y = (int(x) for x in input().split())
    z, w = x + y, x - y
    max_z = max(max_z, z)
    min_z = min(min_z, z)
    max_w = max(max_w, w)
    min_w = min(min_w, w)

print(max(max_z - min_z, max_w - min_w))
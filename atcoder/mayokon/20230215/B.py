N = int(input())
points = []
for _ in range(N):
    x, y = (int(x) for x in input().split())
    points.append((x,y))

for i in range(N):
    x1, y1 = points[i]
    for j in range(i+1, N):
        x2, y2 = points[j]
        ax, ay = x1-x2, y1-y2
        for k in range(j+1, N):
            x3, y3 = points[k]
            bx, by = x1-x3, y1-y3
            mul = abs(ax * bx + ay * by)
            if mul**2 == (ax**2 + ay**2) * (bx**2 + by**2):
                print("Yes")
                exit()

print("No")

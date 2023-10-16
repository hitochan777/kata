def solve():
    cnt = 0
    points = []
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1 = points[i]
            p2 = points[j]

            if p2[0] == p1[0]:
                continue

            if abs((p2[1] - p1[1]) / (p2[0] - p1[0])) <= 1:
                cnt += 1   

    return cnt

print(solve())
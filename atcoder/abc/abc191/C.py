H, W = map(int, input().split())
corners_list = [
    [(-1, 0), (0, -1), (-1, -1)],
    [(1, 0), (0, -1), (1, -1)],
    [(-1, 0), (0, 1), (-1, 1)],
    [(1, 0), (0, 1), (1, 1)],
]
rows = []
for i in range(H):
    rows.append(input())

cnt = 0 
for i in range(1, H-1):
    for j in range(1, W-1):
        c = rows[i][j]
        for corners in corners_list:
            s = set(rows[i+dx][j+dy] for dx, dy in corners)
            if len(s) == 1 and s.pop() != c:
                cnt += 1

print(cnt)
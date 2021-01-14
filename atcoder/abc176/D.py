from collections import deque

walks = [(0, 1), (0, -1), (1, 0), (-1, 0)]
warps = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if [i, j] not in [(0, 0)] + walks]

h, w = list(map(int, input().split()))
ch, cw = list(map(int, input().split()))
dh, dw = list(map(int, input().split()))
ch, cw = ch - 1, cw - 1
dh, dw = dh - 1, dw - 1
rows = []
for _ in range(h):
    rows.append(input())

q = deque()
inf = 10 ** 10
mindist = [[inf] * w for _ in range(h)]
mindist[ch][cw] = 0
q.append(((ch, cw)))
while len(q) > 0:
    pos = q.popleft()
    x, y = pos
    for dx, dy in walks:
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < h and 0 <= ny < w and rows[nx][ny] == ".":
            if mindist[nx][ny] > mindist[x][y]:
                mindist[nx][ny] = mindist[x][y]
                q.appendleft((nx, ny))

    for dx, dy in warps:
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < h and 0 <= ny < w and rows[nx][ny] == ".":
            if mindist[nx][ny] > mindist[x][y] + 1:
                mindist[nx][ny] = mindist[x][y] + 1
                q.append((nx, ny))

if mindist[dh][dw] != inf:
    print(mindist[dh][dw])
else:
    print(-1)
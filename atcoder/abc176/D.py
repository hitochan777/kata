from collections import defaultdict, deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

h, w = list(map(int, input().split()))
ch, cw = list(map(int, input().split()))
dh, dw = list(map(int, input().split()))
ch, cw = ch - 1, cw - 1
dh, dw = dh - 1, dw - 1
rows = []
for _ in range(h):
    rows.append(input())

q = deque()
visited = defaultdict(bool)
mindist = defaultdict(lambda: 10**10)
mindist((ch, cw)) = 0
q.append(((ch, cw), 0))

while len(q) > 0:
    pos, dist = q.popleft()
    if visited[pos]:
        continue

    visited[pos] = True
    x, y = pos
    for i in range(4):
        nextPos = (x + dx[i], y + dy[i])
        if nextPos[0] < 0 or nextPos[0] >= h or nextPos[1] < 0 or nextPos[1] >= w:
            continue

        if rows[nextPos[0]][nextPos[1]] == "#":
            continue

        mindist[nextPos] = min(dist, mindist[nextPos])
        q.appendleft((nextPos, mindist[nextPos]))

    for i in range(-2, 3):
        for j in range(-2, 2):
            nextPos = (x + i, y + j)
            if nextPos[0] < 0 or nextPos[0] >= h or nextPos[1] < 0 or nextPos[1] >= w:
                continue

            if rows[nextPos[0]][nextPos[1]] == "#":
                continue

            mindist[nextPos] = min(dist, mindist[nextPos])
            q.append((nextPos, mindist[nextPos]))

if (dh, dw) in mindist:
    print(mindist[(dh, dw)])
else:
    print(-1)
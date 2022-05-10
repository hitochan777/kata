import sys

H, W, N, M = (int(x) for x in sys.stdin.readline().split())

cells1 = [[0] * W for _ in range(H)]
cells2 = [[0] * W for _ in range(H)]
for _ in range(N):
    x, y = (int(x) for x in sys.stdin.readline().split())
    x, y = x - 1, y - 1
    cells1[x][y] = 1
    cells2[x][y] = 1

for _ in range(M):
    x, y = (int(x) for x in sys.stdin.readline().split())
    x, y = x - 1, y - 1
    cells1[x][y] = 2
    cells2[x][y] = 2

for i in range(H):
    lighted = 0
    for j in range(W):
        if cells1[i][j] == 1:
            lighted = 1
        elif cells1[i][j] == 2:
            lighted = 0

        cells1[i][j] |= lighted

    lighted = 0 
    for j in range(W - 1, -1, -1):
        if cells1[i][j] == 1:
            lighted = 1
        elif cells1[i][j] == 2:
            lighted = 0

        cells1[i][j] |= lighted

for j in range(W):
    lighted = 0
    for i in range(H):
        if cells2[i][j] == 1:
            lighted = 1
        elif cells2[i][j] == 2:
            lighted = 0

        cells2[i][j] |= lighted

    lighted = 0 
    for i in range(H - 1, -1, -1):
        if cells2[i][j] == 1:
            lighted = 1
        elif cells2[i][j] == 2:
            lighted = 0

        cells2[i][j] |= lighted

cnt = sum(1 for i in range(H) for j in range(W) if cells1[i][j] == 1 or cells2[i][j] == 1)
print(cnt)
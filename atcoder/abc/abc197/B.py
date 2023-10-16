directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solve():
    H, W, X, Y = (int(x) for x in input().split())
    rows = []
    for _ in range(H):
        rows.append(input())

    X -= 1
    Y -= 1
    if rows[X][Y] == "#":
        return 0

    cnt = 1
    for direction in directions:
        cur = (X + direction[0], Y + direction[1])
        while cur[0] >= 0 and cur[0] < H and cur[1] >= 0 and cur[1] < W and rows[cur[0]][cur[1]] == ".":
            cnt += 1
            cur = (cur[0] + direction[0], cur[1] + direction[1])

    return cnt


print(solve())
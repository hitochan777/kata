H, W, N, M = (int(x) for x in input().split())

lights = []
for _ in range(N):
    light = tuple(int(x) for x in input().split())
    lights.append(light)

blocks = set()
for _ in range(M):
    block= tuple(int(x) for x in input().split())
    blocks.add(block)

visited = set()
lighted = set()

def visit(x, y, dx, dy):
    if x < 1 or x > H or y < 1 or y > W:
        return

    if (x, y) in visited:
        return

    visited.add((x, y))
    if (x, y) in blocks:
        return

    lighted.add((x, y))
    visit(x + dx, y + dy, dx, dy)

for x, y in lights:
    if (x, y) in visited:
        continue

    visit(x + 1, y, 1, 0)
    visit(x - 1, y, -1, 0)

    visited.add((x, y))
    if (x, y) not in blocks:
        lighted.add((x, y))

visited = set()
for x, y in lights:
    if (x, y) in visited:
        continue

    visit(x, y + 1, 0, 1)
    visit(x, y - 1, 0, -1)

    visited.add((x, y))
    if (x, y) not in blocks:
        lighted.add((x, y))

print(len(lighted))
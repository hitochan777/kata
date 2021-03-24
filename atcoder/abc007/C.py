from collections import deque

R, C = (int(x) for x in input().split())
sy, sx = (int(x) - 1 for x in input().split())
gy, gx = (int(x) - 1 for x in input().split())
rows = []
for i in range(R):
    rows.append(input())

q = deque()
added = set([(sy, sx)])
q.append((sy, sx, 0))
current = (0, 0, 0)
while (current[0], current[1]) != (gy, gx) and len(q) > 0:
    cy, cx, dist = q.popleft()
    current = (cy, cx, dist)
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_pos = (cy + dy, cx + dx, dist + 1)
        if (new_pos[0], new_pos[1]) in added or rows[new_pos[0]][new_pos[1]] == "#":
            continue

        q.append(new_pos)
        added.add((new_pos[0], new_pos[1]))

print(current[2])
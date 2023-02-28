N = int(input())
S = input()
move = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}
cur = (0, 0)
visited = set()
visited.add(cur)
for c in S:
    dx, dy = move[c]
    cur = (cur[0]+dx, cur[1]+dy)
    if cur in visited:
        print("Yes")
        exit()
      
    visited.add(cur)

print("No")


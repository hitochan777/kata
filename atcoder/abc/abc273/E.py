class Node:
  def __init__(self, val, parent):
    self.val = val
    self.parent = parent

pages = {}
p = root = Node(-1, None)
ans = []
Q = int(input())
for _ in range(Q):
  command, *rest = input().split()
  if command == "ADD":
    p = Node(int(rest[0]), p)
  elif command == "DELETE":
    if p.val != -1:
      p = p.parent
  elif command == "SAVE":
    pages[int(rest[0])] = p
  else:
    z = int(rest[0])
    if z in pages:
      p = pages[z]
    else:
      p = root

  ans.append(p.val)
      
print(*ans)
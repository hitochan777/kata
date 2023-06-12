N, M = (int(x) for x in input().split())
visited = set()
visited.add(1)
def dfs(node, parent):
  if node == N:
    print("OK")
    exit()

  _, *v = (int(x) for x in input().split())

  for nb in v:
    if nb not in visited:
      print(nb)
      visited.add(nb)
      dfs(nb, node)

  print(parent)
  _, *v = (int(x) for x in input().split())
  
dfs(1, None)
  
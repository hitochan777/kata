N = int(input())


res = []
def dfs(s="",i=0,c=10,n=10):
  """
  s: current string
  i: largest offset - 1 from "a" till which all charaters are used
  c: number of character types to use
  n: target length of character
  """
  if len(s) == n:
    if i == c:
      res.append(s)

    return

  if n - len(s) < c - i:
    return

  for j in range(i+1):
    dfs(s + chr(ord("a") + j),max(i,j+1),c,n)

for c in range(1,N+1):
  dfs("",0,c,N)


res.sort()
for s in res:
  print(s)
S1 = input()
S2 = input()
S3 = input()

s = list(set(list(S1 + S2 + S3)))
d = {c: i for i, c in enumerate(s)}
if len(s) > 10:
  print("UNSOLVABLE")
  exit()
  
def conv(word, m):
  converted = 0
  for c in word:
    converted *= 10
    converted += m[d[c]]
    
  return converted

def solve(n = 0, m = {}, used = set()):
  if n == len(s):
    n1 = conv(S1, m)
    n2 = conv(S2, m)
    n3 = conv(S3, m)
    if n1 == 0 or n2 == 0 or n3 == 0:
      return
    
    if len(S1) != len(str(n1)) or len(S2) != len(str(n2)) or len(S3) != len(str(n3)):
      return
    
    if n1 + n2 == n3:
      print(n1)
      print(n2)
      print(n3)
      exit()
    
    return
  
  for i in range(10):
    if i in used:
      continue
    
    m[n] = i
    used.add(i)
    solve(n+1, m, used)
    used.remove(i)
    del m[n]
    
solve()
print("UNSOLVABLE")
  
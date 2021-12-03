import sys
N, A, B = (int(x) for x in input().split())
P, Q, R, S = (int(x) for x in input().split())

def is_black1(i, j):
  if i - A != j - B:
    return False

  k = i - A 
  return max(1-A, 1-B) <= k <= min(N-A, N-B)

def is_black2(i,j):
  if i - A != B - j:
    return False

  k = i - A
  return max(1-A, B-N) <= k <= min(N-A, B-1)
  

for i in range(P, Q+1):
  for j in range(R, S+1):
    if is_black1(i,j) or is_black2(i, j):
      sys.stdout.write("#") 
    else:
      sys.stdout.write(".")
  
  sys.stdout.write("\n")
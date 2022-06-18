N, K = (int(x) for x in input().split())
S = input()
def get_winner(a, b):
  if a == b:
    return a

  a, b = sorted([a,b])
  if a == "P":
    if b == "R":
      return "P"
    else:
      return "S"
    
  return "R"

for i in range(K):
  T = S*2
  tmp = []
  for i in range(len(S)):
    tmp.append(get_winner(T[2*i], T[2*i+1]))

  S = "".join(tmp)

print(S[0])

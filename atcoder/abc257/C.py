N = int(input())
S = list(input())
W = list(int(x) for x in input().split())
pairs = sorted(list(zip(W, S)))
acnt = S.count("1")
children = [0]
adults = [0]
for w, a in pairs:
  if a == "0":
    children.append(children[-1]+1)
    adults.append(adults[-1])
  else:
    adults.append(adults[-1]+1)
    children.append(children[-1])
    
i = 0
ans = adults[-1]
# print(children)
# print(adults)
# print(pairs)
while i < N:
  while i < N-1 and pairs[i+1][0] == pairs[i][0]:
    i += 1
    
  cand = children[i+1] + adults[-1] - adults[i+1]
  ans = max(ans, cand)
  # print(ans, i)
  i += 1
  
print(ans)

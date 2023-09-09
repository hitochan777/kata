N, X, Y = (int(x) for x in input().split())

MOD = 840

def ceil(x, y):
  return -(-x // y)

pt = []
for _ in range(N-1):
  P, T = (int(x) for x in input().split())
  pt.append((P,T))

ans = []
for q in range(MOD):
  t = q + X
  for P, T in pt:
    t = ceil(t, P) * P + T

  t += Y
  ans.append(t)

# hoge = [(val, val-i) for i, val in enumerate(ans)]
# print(hoge[0:30])
# print(hoge[30:60])
# print(hoge[60:90])

Q = int(input())
for _ in range(Q):
  q = int(input())
  print(ans[q%MOD] + q // MOD * MOD)
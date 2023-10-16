N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())

a_xor, b_xor = [0] * (N+1), [0] * (N+1)
a_sum, b_sum = [0] * (N+1), [0] * (N+1)
a_cnt, b_cnt = [0] * (N+1), [0] * (N+1)
a_set = set()
b_set = set()

for i, (a, b) in enumerate(zip(A, B), start=1):
  if a not in a_set:
    a_xor[i] = a_xor[i-1] ^ a
    a_sum[i] = a_sum[i-1] + a
  else:
    a_xor[i] = a_xor[i-1]
    a_sum[i] = a_sum[i-1]

  if b not in b_set:
    b_xor[i] = b_xor[i-1] ^ b
    b_sum[i] = b_sum[i-1] + b
  else:
    b_xor[i] = b_xor[i-1]
    b_sum[i] = b_sum[i-1]

  a_set.add(a)
  b_set.add(b)
  a_cnt[i] = len(a_set)
  b_cnt[i] = len(b_set)

Q = int(input())
for _ in range(Q):
  x, y = (int(x) for x in input().split())
  if a_xor[x] == b_xor[y] and a_sum[x] == b_sum[y] and a_cnt[x] == b_cnt[y]:
    print("Yes")
  else:
    print("No")
N = int(input())
A = list(int(x) for x in input().split())
Q = int(input())
for _ in range(Q):
  arr = list(int(x) for x in input().split())
  cmd = arr[0]
  if cmd == 1:
    k, x = arr[1]-1, arr[2]
    A[k] = x
  else:
    k = arr[1]-1
    print(A[k])
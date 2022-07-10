# N = int(input())
# A, B, C = (int(x) for x in input().split())
# A = list(int(x) for x in input().split())

N, M, X, T, D = (int(x) for x in input().split())

if M <= X:
  print(max(D*M + T-X*D,1))
else:
  print(T)
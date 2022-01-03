N = int(input())
A = list(int(x) for x in input().split())
ca = [0]
for i in range(N):
  ca.append(ca[-1] + A[i])

min_val = 10**18
for a in ca[1:-1]:
  min_val = min(min_val, abs(a - (ca[-1] - a)))

print(min_val)

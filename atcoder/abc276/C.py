def is_sorted(A):
  return all(A[i] <= A[i+1] for i in range(len(A) - 1))

def solve(A):
  if is_sorted(A[1:]):
    n = max(a for a in A[1:] if a < A[0])
    return [n] + sorted([a for a in A if a != n], reverse=True)

  return [A[0]] + solve(A[1:])

N = int(input())
P = list(int(x) for x in input().split())
print(*solve(P))
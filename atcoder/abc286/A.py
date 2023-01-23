N, P, Q, R, S = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

B = A[:P-1] + A[R-1:S] + A[Q:R-1]+ A[P-1:Q] + A[S:] 
print(*B)
N = int(input())
B = list(int(x)-i-1 for i, x in enumerate(input().split()))
B.sort()
median = B[N//2]
ans = sum(abs(b - median) for b in B)
print(ans)




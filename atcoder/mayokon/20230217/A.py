N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = set(int(x)-1 for x in input().split())
mx = max(A)
if any(a == mx and i in B for i, a in enumerate(A)):
    print("Yes")
else:
    print("No")
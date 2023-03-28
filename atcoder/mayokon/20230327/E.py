N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split()).sort()
F = list(int(x) for x in input().split()).sort(reverse=True)

def achievable(k):
    return False

ng, ok = -1, 10**18
while ok - ng > 1:
    k = (ok + ng) // 2
    if achievable(k):
        ok = k
    else:
        ng = k

print(ok)
    
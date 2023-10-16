N, K = (int(x) for x in input().split())

def f(n):
    s = "".join(sorted(list(str(n))))
    # print(s)
    g1 = int(s[::-1])
    g2 = int(s)
    return g1 - g2

cur = N
for i in range(K):
    cur = f(cur)

print(cur)

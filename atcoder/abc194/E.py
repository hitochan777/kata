def solve(N, M, A):
    pre = list([] for _ in range(N))
    for i, a in enumerate(A):
        pre[a].append(i)

    for i in range(N):
        pre[i].append(N)
        prev = -1
        for pos in pre[i]:
            if pos - prev > M:
                return i

            prev = pos

    return N

N, M = list(int(x) for x in input().split())
A = list(int(x) for x in input().split())

ans = solve(N, M, A)
print(ans)
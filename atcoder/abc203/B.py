N, K = (int(x) for x in input().split())

ans = ((N * (N + 1)) // 2 * 100) * K + (K * (K + 1) // 2) * N
print(ans)

# 101 + 102 + 100
# 201 + 202 + 200
# 301 + 302 + 300
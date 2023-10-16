def solve(L, R):
    if R - L < L:
        return 0

    return (R - 2 * L + 1) * (R - L + 1) - (R - L) * (R - L + 1) // 2 + L * (L - 1) // 2

T = int(input())
for _ in range(T):
    L, R = (int(x) for x in input().split())
    print(solve(L, R))
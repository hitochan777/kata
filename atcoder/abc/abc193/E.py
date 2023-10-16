from atcoder import math

def solve(x: int, y: int, p: int, q: int) -> str:
    C, D = (x + y) * 2, p + q
    min_val = 1 << 64
    for i in range(x, x + y):
        for j in range(p, p + q):
            t, lcm = math.crt([i, j], [C, D])
            print((t, lcm))
            if lcm > 0:
                min_val = min(min_val, t)

    return str(min_val) if min_val < (1 << 64) else "infinity"

T = int(input())
for _ in range(T):
    x, y, p, q = (int(x) for x in input().split())
    ans = solve(x, y, p, q)
    print(ans)

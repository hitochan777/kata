X = int(input())
M = int(input())

def to_base(x, b, M):
    s = str(x)[::-1]
    n = len(s)
    pow = 1
    total = 0
    for i in range(0, n):
        total += int(s[i]) * pow
        pow *= b
        if total > M:
            return M + 1

    return total

def solve(X, M):
    if X % 10 == X:
        if X <= M:
            return 1
        else:
            return 0

    largest = int(sorted(list(str(X)))[-1])
    # digits = len(str(X))
    l, h = largest + 1, 10**18
    highest = largest

    while l <= h:
        m = (l + h) >> 1
        decoded = to_base(X, m, M)
        # print((l, h, m, decoded))
        if decoded > M:
            h = m - 1
        elif decoded == M:
            # print("hoge")
            return m - largest
        else:
            l = m + 1
            highest = m

    return highest - largest

ans = solve(X, M)    
print(ans)

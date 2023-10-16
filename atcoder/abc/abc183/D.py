def solve():
    n, w = map(int, input().split())
    table = [0] * 200001
    for _ in range(n):
        s, t, p = map(int, input().split())
        table[s] += p
        table[t] -= p

    for i in range(0, 200001):
        if i > 0:
            table[i] += table[i-1]

        if table[i] > w:
            return False

    return True

print("Yes" if solve() else "No")
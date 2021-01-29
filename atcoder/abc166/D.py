def solve(X):
    for x in range(-200, 201):
        for y in range(-200, 201):
            if x**5 - y**5 == X:
                return (x, y)

    return (None, None)

X = int(input())
ans = solve(X)
print(f"{ans[0]} {ans[1]}")

def get_expectation(x, y, z, memo):
    if x >= 100 or y >= 100 or z >= 100:
        return 0
    
    if (x, y, z) in memo:
        return memo[(x, y, z)]

    n = x + y + z
    memo[(x, y, z)] = x / n * (get_expectation(x + 1, y, z, memo) + 1) + y / n * (get_expectation(x, y + 1, z, memo) + 1) + z / n * (get_expectation(x, y, z + 1, memo) + 1)

    return memo[(x, y, z)]

memo = {}
a, b, c = map(int, input().split())
print(get_expectation(a, b, c, memo))
n = int(input())

def is_unlucky(x):
    return "7" in str(x) or "7" in oct(x)

count = sum(1 for x in range(1, n + 1) if not is_unlucky(x))
print(count)

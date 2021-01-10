from collections import Counter

def issubset(a, b):
    for d, c in a.items():
        if d not in b or b[d] < c:
            return False

    return True

def solve():
    s = input()
    n = min(len(s), 3)
    
    sc = Counter(s)
    multiples = [Counter(str(i * 8)) for i in range(10 ** (n-1) // 8 + 1, (10 ** n - 1) // 8 + 1)]
    return any(issubset(multiple, sc) for multiple in multiples)

print("Yes" if solve() else "No")
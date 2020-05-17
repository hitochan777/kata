
def solve():
    n, s = list(map(int, input().split()))
    if s // n == 1:
        print("NO")
        return
    
    num = s // n
    print("YES")
    nums = [num] * n
    nums[-1] += s % n
    print(" ".join(map(str, nums)))
    print(1)


solve()


def solve(a1, k):
    a = a1
    for _ in range(k-1):
        li = list(map(int, list(str(a))))
        new_a = a + min(li) * max(li)
        if new_a == a:
            return a

        a = new_a

    return a

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a1, k = map(int, input().split())
        ans = solve(a1, k)
        print(ans)

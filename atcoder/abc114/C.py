N = int(input())

def find(n: str, N: int):
    if int(n) > N:
        return 0

    cnt = 0
    if "3" in n and "5" in n and "7" in n:
        cnt += 1

    cnt += find(n + "3", N)
    cnt += find(n + "5", N)
    cnt += find(n + "7", N)
    return cnt

print(find("0", N))
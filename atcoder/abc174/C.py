def solve():
    K = int(input())
    prev = 7 % K
    cnt = 1
    if prev == 0:
        return cnt

    for i in range(1, K):
        prev = (10 * prev + 7) % K
        cnt += 1
        if prev == 0:
            return cnt

    return -1

print(solve())

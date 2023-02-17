from functools import reduce
N = int(input())
A = list(int(x) for x in input().split())

xor = reduce(lambda a, b: a^b, A, 0)
ans = []
for a in A:
    ans.append(xor ^ a)

print(*ans)
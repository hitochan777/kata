from itertools import permutations

S, K = (x for x in input().split())
K = int(K)

perms = list(set(permutations(S)))
perms.sort()
print("".join(perms[K-1]))
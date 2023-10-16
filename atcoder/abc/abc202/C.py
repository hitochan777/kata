from collection import defaultdict

n = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = set(int(x) for x in input().split())

A_dict = defaultdict(set)
B_dict = defaultdict(set)

for i, x in enumerate(A):
    A_dict[x].add(i)

for i, x in enumerate(B):
    if i in C:
        B_dict[x].add(i)
from collections import Counter

N = int(input())
A = Counter(int(x) % 200 for x in input().split())
print(sum(v * (v-1) // 2 for k, v in A.items()))
from collections import Counter
N = int(input())
A = list(int(x) for x in input().split())
cnts = Counter(A)

if N % 2 == 0:
  if any(cnts[i] != 2 for i in range(1, N, 2)):
    print(0)
    exit()
else:
  if cnts[0] != 1 or any(cnts[i] != 2 for i in range(2, N, 2)):
    print(0)
    exit()

print(pow(2, N//2, 10**9 + 7))
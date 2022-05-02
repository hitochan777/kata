N, K = (int(x) for x in input().split())
D = set(int(x) for x in input().split())

for i in range(N, 10**5):
  if all(int(c) not in D for c in str(i)):
    print(i)
    exit()

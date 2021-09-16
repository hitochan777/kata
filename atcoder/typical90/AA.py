N = int(input())
registered = set()
for i in range(N):
  S = input()
  if S not in registered:
    registered.add(S)
    print(i+1)
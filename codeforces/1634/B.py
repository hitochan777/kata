t = int(input())
for _ in range(t):
  n, x, y = (int(x) for x in input().split())
  parity = sum(int(x) for x in input().split()) % 2
  if (x + parity) % 2 == y % 2:
    print("Alice")
  else:
    print("Bob")

  

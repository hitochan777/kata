D = int(input())
X = int(input())
stocks = [X]
for _ in range(D-1):
  A = int(input())
  stocks.append(stocks[-1]+A)

Q = int(input())
for _ in range(Q):
  S, T = (int(x)-1 for x in input().split())
  if stocks[S] == stocks[T]:
    print("Same")
  elif stocks[S] > stocks[T]:
    print(S+1)
  else:
    print(T+1)
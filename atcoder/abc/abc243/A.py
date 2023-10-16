V, A, B, C = (int(x) for x in input().split())

while True:
  if V < A:
    print("F")
    exit()

  V -= A
  if V < B:
    print("M")
    exit()

  V -= B
  if V < C:
    print("T")
    exit()

  V -= C
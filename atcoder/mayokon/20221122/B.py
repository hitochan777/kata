A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0
for a in range(0,A+1):
  for b in range(0,B+1):
    for c in range(0,C+1):
      if 500*a + 100*b + 50*c == X:
        cnt += 1  

print(cnt)
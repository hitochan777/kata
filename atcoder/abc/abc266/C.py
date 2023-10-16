def CrossProduct(A):
    X1 = (A[1][0] - A[0][0])
    Y1 = (A[1][1] - A[0][1])
    X2 = (A[2][0] - A[0][0])
    Y2 = (A[2][1] - A[0][1])
    return (X1 * Y2 - Y1 * X2)
 
def isConvex(points):
    N = len(points)
    prev = 0
    curr = 0
    for i in range(N):
        temp = [points[i], points[(i + 1) % N],
                           points[(i + 2) % N]]
 
        curr = CrossProduct(temp)
        if (curr != 0):
            if (curr * prev < 0):
                return False
            else:
                prev = curr
 
    return True

A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = list(int(x) for x in input().split())
D = list(int(x) for x in input().split())
if isConvex([A, B, C, D]):
  print("Yes")
else:
  print("No")
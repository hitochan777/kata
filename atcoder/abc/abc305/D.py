from bisect import bisect_left, bisect_right
N = int(input())
A = list(int(x) for x in input().split())
A.append(10**18)

accs = [[0], [0]]
for i in range(1, len(A)):
  accs[i%2].append(accs[i%2][-1] + (A[i] - A[i-1]))
  accs[(i+1)%2].append(accs[(i+1)%2][-1])

sleeps = accs[0]
awakes = accs[1]

Q = int(input())
for _ in range(Q):
    l, r = (int(x) for x in input().split())
    li = bisect_left(A, l)
    ri = bisect_right(A, r)
    sleep = 0
    # print(li, A[li], ri, A[ri])
    if li % 2 == 0: # sleep
      sleep += A[li] - l

    if ri % 2 == 0: # sleep
      sleep += r - A[ri]

    sleep += sleeps[ri] - sleeps[li]
    print(sleep)
       
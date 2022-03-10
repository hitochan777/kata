from collections import deque
N = int(input())
li = []
for _ in range(N):
  A = int(input())
  li.append(A)

li.sort()
queue = deque()
p = [0, N-1]
queue.append(li[0])
for i in range(1,N):
  if (i // 2) % 2 == 0:
    queue.append(li[p[i%2]])
  else:
    queue.appendleft(li[p[i%2]])

  if i % 2 == 0:
    p[i%2] += 1
  else:
    p[i%2] -= 1

total = 0
prev = None
while len(queue) > 0:
  val = queue.pop()
  print(val)
  if prev != None:
    total += abs(prev - val)

  prev = val

print(total)



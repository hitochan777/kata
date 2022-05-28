from collections import defaultdict
import heapq

class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
          return
        else:
            self.d[x]-=1

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]


ms_max = HeapDict()
ms_min = HeapDict()
cnt = defaultdict(int)
max_val, min_val = 0, 10**18
Q = int(input())
for _ in range(Q):
  vals = list(int(x) for x in input().split())
  if vals[0] == 1:
    if cnt[vals[1]] == 0:
      ms_max.insert(-vals[1])
      ms_min.insert(vals[1])

    cnt[vals[1]] += 1
  elif vals[0] == 2:
    cnt[vals[1]] -= min(cnt[vals[1]], vals[2])
    if cnt[vals[1]] == 0:
      ms_max.erase(-vals[1])
      ms_min.erase(vals[1])
      del cnt[vals[1]]
  else:
    print(-ms_max.get_min() - ms_min.get_min())
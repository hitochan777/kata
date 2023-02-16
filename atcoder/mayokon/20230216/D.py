from collections import Counter
N = int(input())
A = list(int(x) for x in input().split())
cnt = Counter(A)
nums = sorted([(k, v) for k, v in cnt.items()])

acc = [0]
for _, val in nums:
    acc.append(acc[-1]+val)

ans = 0
for i, (val, freq) in enumerate(nums):
  # print(freq, acc[i],(acc[-1] - acc[i+1]))
  ans += freq * acc[i] * (acc[-1] - acc[i+1])

print(ans)
  


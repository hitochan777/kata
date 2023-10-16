from collections import Counter
n = int(input())
nums = input().split()
c = Counter(nums)

total = sum(v * (v - 1) // 2 for k, v in c.items()) 

for num in nums:
    val = c[num]
    adjusted = total - val * (val - 1) // 2 + (val - 1) * (val - 2) // 2
    print(adjusted)
from collections import Counter
n = int(input())
nums = input().split()
c = Counter(nums)

for num in nums:
    c[num] -= 1
    total = 0
    for k, v in c.items():
        total += v * (v - 1) // 2

    c[num] += 1
    print(total)


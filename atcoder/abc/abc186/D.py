
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
sums = [0]
for num in nums:
    sums.append(sums[-1] + num)


total = 0
for i in range(n):
   total += sums[-1] - sums[i+1] - (n - i - 1) * nums[i]

print(total)

# \sum_{j=i+1}^{N} a_j - (N - i) * a_i
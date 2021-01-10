n = int(input())
nums = list(map(int, input().split()))

max_step, max_pos, pos, sum_pos = (0, 0, 0, 0)
for i in range(n):
    max_step = max(max_step, sum_pos + nums[i])
    max_pos = max(max_pos, pos + max_step)
    pos += sum_pos + nums[i]
    sum_pos += nums[i]
    # print((max_step, max_pos, pos, sum_pos))

print(max_pos)
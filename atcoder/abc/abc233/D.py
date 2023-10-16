# public class Solution {
#     public int subarraySum(int[] nums, int k) {
#         int count = 0, sum = 0;
#         HashMap < Integer, Integer > map = new HashMap < > ();
#         map.put(0, 1);
#         for (int i = 0; i < nums.length; i++) {
#             sum += nums[i];
#             if (map.containsKey(sum - k))
#                 count += map.get(sum - k);
#             map.put(sum, map.getOrDefault(sum, 0) + 1);
#         }
#         return count;
#     }
# }

from collections import defaultdict

d = defaultdict(int)
N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

cnt = 0
total = 0
d[0] = 1
for a in A:
  total += a
  cnt += d[total - K]
  d[total] = d[total] + 1

print(cnt)

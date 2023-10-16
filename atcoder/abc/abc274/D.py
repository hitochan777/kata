def knapSack(nums, S):
    sum = 0;
    for i in range(len(nums)):
        sum += nums[i];
 
    # If target + sum is odd or S exceeds sum
    if (sum < S or -sum > -S or
       (S + sum) % 2 == 1):
 
        # No sultion exists
        return 0;
       
    dp = [0]*(((S + sum) // 2) + 1);
    dp[0] = 1;
    for j in range(len(nums)):
        for i in range(len(dp) - 1, nums[j] - 1, -1):
            dp[i] += dp[i - nums[j]];
         
    # Return the answer
    return dp[len(dp) - 1];


N, x, y = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

evens = [a for i, a in enumerate(A) if i > 0 and i % 2 == 0]
odds = [a for i, a in enumerate(A) if i % 2 != 0]


if knapSack(evens, abs(x - A[0])) > 0 and knapSack(odds, abs(y)) > 0:
  print("Yes")
else:
  print("No")



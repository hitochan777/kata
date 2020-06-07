from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        if len(coins) == 0 or amount < 0:
            return 0
    
        coin = coins[0]
        cnt = 0
        comb = 0
        print(f"{amount=} {coins=}")
        while coin * cnt <= amount:
            comb += self.change(amount - coin * cnt, coins[1:])
            cnt += 1
            
        return comb

if __name__ == "__main__":
    solver = Solution()
    print(solver.change(500, [3,5,7,8,9,10,11]))


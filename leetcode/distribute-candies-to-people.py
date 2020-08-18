class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        num_candies = 1
        p = 0
        while candies > 0:
            ans[p] += min(num_candies, candies)
            candies -= num_candies
            num_candies += 1
            p = (p + 1) % num_people
        
        return ans

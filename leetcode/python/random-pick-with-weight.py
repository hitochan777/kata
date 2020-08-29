from typing import List 
import random

class Solution:

    def __init__(self, w: List[int]):
        self.population = list(range(len(w)))
        total = sum(w)
        self.weights = [item / total for item in w]
                
    def pickIndex(self) -> int:
        return random.choices(self.population, self.weights, k=1)[0]

if __name__ == "__main__":
    solver = Solution([3,14,1,7])
    for _ in range(100):
        print(solver.pickIndex())

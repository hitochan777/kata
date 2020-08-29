class Solution:
    def n_choose_k(self, n, k):
        return factorial(n) // (factorial(k) * factorial(n-k))
        
    def getRow(self, rowIndex: int) -> List[int]:
        return [self.n_choose_k(rowIndex, i) for i in range(rowIndex+1)]

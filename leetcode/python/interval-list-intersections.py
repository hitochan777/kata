class Solution:
    def find_intersection(self, a, b):
        if a[1] < b[0] or a[0] > b[1]:
            return None
        
        return [max(a[0], b[0]), min(a[1], b[1])]
    
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        p, q = 0, 0
        ans = []
        while p < len(A) and q < len(B):
            ins = self.find_intersection(A[p], B[q])
            if ins is not None:
                ans.append(ins)
            
            if A[p][1] < B[q][1]:
                p += 1
            elif A[p][1] > B[q][1]:
                q += 1
            else:
                p += 1
                q += 1
                
        return ans

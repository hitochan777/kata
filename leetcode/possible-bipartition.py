class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        m = defaultdict(list)
        for p1, p2 in dislikes:
            m[p1].append(p2)
            m[p2].append(p1)
        
        colors = {}
        
        def colorable(node, c) -> bool:
            pass
        
        return all(colorable(node, 0) for n in range(1, N+1) if n not in colors)

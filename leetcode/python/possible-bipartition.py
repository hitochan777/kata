class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        m = defaultdict(list)
        for p1, p2 in dislikes:
            m[p1].append(p2)
            m[p2].append(p1)
        
        colors = {}
        
        def colorable(node, c) -> bool:
            if node in colors:
                return colors[node] == c
            
            colors[node] = c
            return all(colorable(neighbor, c ^ 1) for neighbor in m[node])
        
        return all(colorable(n, 0) for n in range(1, N+1) if n not in colors)

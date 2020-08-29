class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for tgt, src in prerequisites:
            graph[src].append(tgt)
            
        taken = defaultdict(bool)
        stack = defaultdict(bool)
        
        def find_loop(node) -> bool:
            if stack[node]:
                return True
            
            if taken[node]:
                return False
            
            taken[node], stack[node] = True, True
            exist_loop = any(find_loop(neighbor) for neighbor in graph[node])
            stack[node] = False
            return exist_loop
            
        for node in range(0, numCourses):
            taken = defaultdict(bool)
            stack = defaultdict(bool)
            if find_loop(node):
                return False
            
        return True

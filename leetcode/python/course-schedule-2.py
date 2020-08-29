class Solution:
    def dfs(self, num, graph, visited, local_visited):
        if local_visited[num]:
            return [], False
            
        if visited[num]:
            return [], True
        
        courses = []
        visited[num] = True
        local_visited[num] = True
        for i in graph[num]:
            subcourses, ok  = self.dfs(i, graph, visited, local_visited)
            if not ok:
                return [], False
            
            courses += subcourses
        
        del local_visited[num]
        return courses + [num], True
        
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = defaultdict(int)
        for src, tgt in prerequisites:
            graph[src].append(tgt)
            
        courses = []
        for num in range(numCourses):
            local_visited = defaultdict(int)
            subcourses, ok = self.dfs(num, graph, visited, local_visited)
            if not ok:
                return []
            
            courses += subcourses
                
        return courses

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0:
            return
        
        visited = defaultdict(str)
        targets = []
        
        def _dfs(x, y) -> None:
            
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return

            if visited[f"{x},{y}"]:
                return
            
            visited[f"{x},{y}"] = True
            if board[x][y] == "O":
                board[x][y] = "#"
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)
                
        def dfs(x, y) -> None:
            print(f"{x=} {y=}")
            if board[x][y] != "O":
                return
            
            _dfs(x, y)
        
        """
        OOO
        OOO
        OOO
        """
        
        
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)
        
        for i in range(1,len(board[0])-1):
            dfs(0, i)
            dfs(len(board)-1, i)
            
        print(board)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            

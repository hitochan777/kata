class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N>14:
            N = N%14 + 14
        
        for n in range(N):
            next_cells = cells[:]
            next_cells[0] = next_cells[-1] = 0
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    next_cells[i] = 1
                else:
                    next_cells[i] = 0
               
            cells = next_cells
            
        return cells

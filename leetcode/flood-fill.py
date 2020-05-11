from collections import defaultdict

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = defaultdict(bool)
        start_color = image[sr][sc]
        
        
        def traverse(image: List[List[int]], x: int, y: int, newColor: int) -> List[List[int]]:
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return
            
            if visited[(x, y)]:
                return
            
            visited[(x, y)] = True
            if image[x][y] == start_color:
                    image[x][y] = newColor
            else:
                return
                    
            dvs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dv in dvs:
                c = (x + dv[0], y + dv[1])
                traverse(image, c[0], c[1], newColor)
            
        traverse(image, sr, sc, newColor)
        return image

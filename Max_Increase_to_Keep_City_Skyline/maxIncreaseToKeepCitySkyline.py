class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        verticalMaxes = self.findVerticalMaxes(grid)
        print(verticalMaxes)
        horizontalMaxes = self.findHorizontalMaxes(grid)
        print(horizontalMaxes)
        
    
    def findVerticalMaxes(self, grid):
        
        y = 0
        max_list = []
        

        for line in grid:
            currMax = 0 
            for num in grid[y]:
                if num > currMax:
                    currMax = num
            max_list.append(currMax)
            y = y+1
        return max_list
        
        
    def findHorizontalMaxes(self, grid):
        
        x = 0
        y = 0
        max_list = []
        
        for line in grid[x]:
            currMax = 0
            for num in grid[y]:
                if num > currMax:
                    currMax = num
                y = y + 1
            max_list.append(currMax)
            x = x + 1
    
        
        return []
        
      
        

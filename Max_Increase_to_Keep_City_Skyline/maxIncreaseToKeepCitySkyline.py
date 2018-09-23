class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        verticalMaxes = self.findVerticalMaxes(grid)
        horizontalMaxes = self.findHorizontalMaxes(grid)
        
        maxIncrease = 0
        for x, row in enumerate(grid):
            for y, column in enumerate(grid[0]):
                minFromMaxLists = min([verticalMaxes[x], horizontalMaxes[y]])
                increaseAmount = minFromMaxLists - grid[x][y]
                maxIncrease = maxIncrease + increaseAmount
        return maxIncrease
    
    
    def findVerticalMaxes(self, grid):
        
        column = 0
        max_list = []
        
        for row in grid:
            currMax = 0 
            for num in grid[column]:
                if num > currMax:
                    currMax = num
            max_list.append(currMax)
            column = column+1
        return max_list
        
        
    def findHorizontalMaxes(self, grid):
        
        max_list = []
        currColumn = 0
        
        for outRow in grid:
            currMax = 0
            currRow = 0
            for inRow in grid:
                num = grid[currRow][currColumn]
                if num > currMax:
                    currMax = num
                currRow = currRow + 1
            max_list.append(currMax)
            currColumn = currColumn + 1

        return max_list

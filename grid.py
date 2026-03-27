import numpy as np
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row = len(grid) 
        col = len(grid[0]) 
        total = np.sum(grid)
        rowsum = 0 
        for i in range(row) : 
            for j in range(col) : 
                rowsum = rowsum + grid[i][j] 
            if(rowsum == (total - rowsum)) : 
                return True 
        colsum = 0 
        for i in range(col) : 
            for j in range(row) : 
                colsum = colsum + grid[j][i] 
            if(colsum == (total - colsum)) : 
                return True 
        return False   
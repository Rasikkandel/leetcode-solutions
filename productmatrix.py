''' Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:

Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
Return the product matrix of grid. ''' 

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mul = 1 
        row = len(grid) 
        col = len(grid[0]) 
        product = [[0]*col for _ in range(row)]
        for i in range(row) : 
            for j in range(col): 
                mul = mul * grid[i][j] 
        
        for i in range(row) : 
            for j in range(col) : 
                product[i][j] = (mul // grid[i][j]) % 12345 
        
        return product

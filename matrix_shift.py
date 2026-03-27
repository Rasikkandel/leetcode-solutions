''' You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

The following proccess happens k times:

Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.


Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.


Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.'''

def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        row = len(mat) 
        col = len(mat[0]) 
        shift = k % col 
        if(shift == 0) : 
            return True 
        for i in range(row) : 
            row = mat[i] 
            shifted_row = mat[i][:]
            if(i % 2 == 0) : 
                shifted_row = row[shift:] + row[:shift] 
            else : 
                shifted_row = row[-shift:] + row[:-shift] 
            if(row != shifted_row) : 
                return False
                     
        return True
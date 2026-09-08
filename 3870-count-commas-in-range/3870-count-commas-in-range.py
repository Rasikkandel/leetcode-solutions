class Solution:
    def countCommas(self, n: int) -> int:
        size = len(str(abs(n)))
        if size < 4 : 
            return 0 
        return int(n) - 999
        
        
class Solution:
    def countCommas(self, n: int) -> int:
        """ 
        if(n < 1000): 
            return 0 
        elif (n >= 1000 and n < 1000000) : 
            return n - 999 
        elif (n >= 1000000 and n < 1000000000) : 
            count = n - 999 
            count += n - 999999
        elif (n >= 1000000000 and n < 1000000000000) : 
            count = n - 999
            count += n - 999999
            count += n - 999999999
        elif(n >= 1000000000000 and n < 1000000000000000) : 
            count = n - 999
            count += n - 999999
            count += n - 999999999
            count += n - 999999999999
        else : 
            count = n - 999
            count += n - 999999
            count += n - 999999999
            count += n - 999999999999
            count += n - 999999999999999
        
        return count
        """
        p = 1000
        res = 0 
        while p <= n : 
            res += n - p + 1 
            p = p * 1000
        return res 

        
        
class Solution:
    def pivotInteger(self, n: int) -> int:
        prefixsum = 0 
        suffixsum = (n * (n+1)) // 2  
        for i in range(1,n+1) :
            prefixsum += i 
            if(prefixsum == suffixsum) : 
                return i 
            suffixsum -= i 
        return -1 
            
        
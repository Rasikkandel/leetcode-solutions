class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0  
        orig = x 
        if(x < 0) : 
            return False
        while(orig != 0): 
            last_elem = orig % 10 
            rev = rev * 10 + last_elem 
            orig = orig // 10  
        if (rev == x) : 
            return True 
        return False 


        """ BY converting to string
        return str(x) == str(x)[::-1]
        """ 
        
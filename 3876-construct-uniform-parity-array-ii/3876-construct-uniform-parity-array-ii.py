class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_ele = nums1[0]
        even_count = 0 
        odd_count = 0 
        n = len(nums1)
        for i in nums1 : 
            if(i%2==0) : 
                even_count += 1 
            else : 
                odd_count += 1
            if(i < min_ele) : 
                min_ele = i 
        
        if(even_count == n or odd_count == n) : 
            return True 
        
        elif(min_ele % 2 == 1) : 
            return True
        return False

""" pythonic approach 
    n = len(nums1)
        odd_count = sum(x % 2 for x in nums1)
        
        if odd_count == 0 or odd_count == n:
            return True
        
        return min(nums1) % 2 == 1
""" 


        

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums) 
        target = sum(nums) - x 
        left = 0 
        value = 0 
        if target < 0 : 
            return -1 
        if target == 0 : 
            return n 
        
        best_max = -1 


        for right in range(0,n) : 
            value += nums[right] 
            while(value > target) : 
                value -= nums[left] 
                left += 1 
            if (value == target) : 
                best_max = max(best_max , right - left + 1)

        return -1 if best_max == -1 else  n - best_max 
        

            
            


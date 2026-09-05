class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums) 
        suffix_min = [0]*n  
        suffix_min[-1] = nums[n-1]
        for j in range(n-2,-1,-1) : 
            suffix_min[j] = min(suffix_min[j+1] , nums[j]) 
        
        maxvalue = 0 
        for i in range(n) : 
            maxvalue = max(maxvalue , nums[i])
            score = maxvalue - suffix_min[i] 
            if score <= k : 
                return i 

        return -1
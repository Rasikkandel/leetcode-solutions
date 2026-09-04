class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_stable = n 
        for i in range(n) : 
            max_prefix = 0 
            min_suffix = float('inf') 
            for j in range(i+1) : 
                max_prefix = max(nums[j] , max_prefix) 
            for j in range(i,n) : 
                min_suffix = min(min_suffix , nums[j]) 
            score = max_prefix - min_suffix 
            if( i < min_stable and score <= k) : 
                min_stable = i 
        if(min_stable == n) : 
            return -1 
        return min_stable 
             

            
        
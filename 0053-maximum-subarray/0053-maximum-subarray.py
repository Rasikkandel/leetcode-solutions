class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float('-inf')   
        n = len(nums)  
        sum = 0  
        for i in range(n) : 
            sum += nums[i]  
            if(sum > max ) : max = sum 
            if(sum < 0) : 
                sum = 0 
        return max 
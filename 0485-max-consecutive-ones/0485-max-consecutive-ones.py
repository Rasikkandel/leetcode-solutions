class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum = 0 
        max = 0 
        for i in range(len(nums)) : 
            sum += nums[i] 
            if(sum > max) : 
                max = sum 
            if(nums[i] == 0) : 
                sum = 0 
        return max 


        
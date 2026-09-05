class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0 
        nums.sort() 
        n = len(nums) 
        count = 1  
        longest = 1  
        for i in range(1,n) : 
            if(nums[i] ==  nums[i-1] + 1) : 
                count += 1 
            elif (nums[i] == nums[i-1]) : 
                continue 
            else : 
                count = 1 
            longest = max(count , longest) 

        return longest 

            

        
""" Brute solution :: 
def longestConsecutive(self, nums):
        if not nums : 
            return 0 
        longest = 1 
        for i in range(len(nums)) : 
            current_number = nums[i] 
            current_streak = 1 
            while (current_number + 1) in nums : 
                current_number += 1 
                current_streak += 1 
            longest = max(current_streak , longest) 
        return longest
        """ 
"""
## better 
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
        return longest """

#optimal
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)  
        longest = 0 
        for num in nums_set : 
            if ((num - 1) in nums_set) : 
                continue 
            current = num 
            count = 1
            while (current + 1 ) in nums_set :
                current += 1
                count += 1
            longest = max(longest , count)
        return longest

            

        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() 
        n = len(nums) 
        count = 0  
        longest = 0  
        last_elem_in_seq = float('-inf')
        for i in range(n) : 
            if(nums[i] == last_elem_in_seq + 1) : 
                count += 1 
                longest = max(longest , count) 
                last_elem_in_seq = nums[i] 
            elif (nums[i] == last_elem_in_seq) : 
                continue 
            else : 
                count = 1 
                last_elem_in_seq = nums[i] 
            longest = max(count , longest) 

        return longest 

            

        
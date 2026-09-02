class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {} 
        n = len(nums) 
        for i in nums : 
            if i in num_count : 
                num_count[i] += 1 
            else : 
                num_count[i] = 1 
        for key in num_count.keys() : 
            if(num_count[key] > n/2) : 
                return key 
        return -1

        

        
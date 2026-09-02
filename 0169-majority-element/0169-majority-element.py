class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = 0
        count = 0 
        n = len(nums)
        for i in range(n) : 
            if count == 0 : 
                count = 1 
                elem = nums[i] 
            elif(nums[i] == elem) : 
                count += 1
            else : 
                count -= 1 
        
        max_count = 0 
        for i in nums : 
            if(i == elem) : 
                max_count += 1 
        
        if(max_count > n/2 ) : 
            return elem 
        return -1


        

        
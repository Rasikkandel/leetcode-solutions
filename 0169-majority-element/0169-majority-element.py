class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = 0 
        count = 0 
        for i in range(len(nums)) : 
            if(count == 0) : 
                elem = nums[i] 
                count = 1 
            elif(nums[i] == elem) : 
                count += 1
            else : 
                count -= 1 
        ## if majority element exist na garna pani sakxa then yo steps leh check garni 
        """ max_count = 0 
        for i in nums : 
            if(i == elem) : 
                max_count += 1 
        
        if(max_count > n/2 ) : 
            return elem  
        return -1
        """ 
        return elem 


        

        
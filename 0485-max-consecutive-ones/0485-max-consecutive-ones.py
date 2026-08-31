class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        max_consecutive = 0 
        for i in nums : 
            if(i==1) : 
                counter += 1 
                max_consecutive = max(max_consecutive , counter) 
            else : 
                counter = 0 
        return max_consecutive
                

        
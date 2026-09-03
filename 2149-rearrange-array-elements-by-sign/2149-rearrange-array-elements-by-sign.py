class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0 
        neg = 1 
        temp = [0] * len(nums) 
        for i in range(len(nums)) : 
            if(nums[i] < 0) : 
                temp[neg] = nums[i] 
                neg += 2 
            else : 
                temp[pos] = nums[i] 
                pos += 2
        
        return temp
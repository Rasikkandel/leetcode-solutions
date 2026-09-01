class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i in range(len(nums)) : 
            another_num = target - nums[i]
            if another_num in hashmap : 
                return [ hashmap[another_num] , i ] 
            hashmap[nums[i]] = i 
        
        
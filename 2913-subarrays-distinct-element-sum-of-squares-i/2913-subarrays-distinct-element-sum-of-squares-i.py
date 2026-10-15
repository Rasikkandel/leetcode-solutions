class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums) 
        ans = 0 
        for i in range(n) : 
            unique_set = set() 
            for j in range(i,n) : 
                unique_set.add(nums[j]) 
                ans += len(unique_set) ** 2 
        return ans


        
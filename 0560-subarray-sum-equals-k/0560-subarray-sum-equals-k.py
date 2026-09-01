class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {} 
        total = 0 
        count = 0 
        for i in range(len(nums)) :
            total += nums[i] 
            if(total == k) : 
                count += 1 

            rem = total - k 
            if rem in prefix_sums : 
                count += prefix_sums[rem] 
            if total in prefix_sums : 
                prefix_sums[total] += 1 
            else : 
                prefix_sums[total] = 1  
            
        return count


        
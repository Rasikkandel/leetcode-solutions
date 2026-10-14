class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # better approach 
        """
        n = len(nums) 
        ans = set() 
        for i in range(n) : 
            hashmap = set() 
            for j in range(i+1,n) : 
                k = -(nums[i] + nums[j]) 
                if k in hashmap : 
                    ans.add(tuple(sorted((nums[i],nums[j],k))))
                hashmap.add(nums[j]) 
        return [list(item) for item in ans] 
        """
        #optimal approach
        n = len(nums) 
        ans = [] 
        nums.sort() 
        for i in range(n) : 
            if(i>0 and nums[i] == nums[i-1]) : 
                continue 
            j = i + 1 
            k  = n - 1 
            while(j < k) : 
                result = nums[i] + nums[j] + nums[k]  
                if(result < 0) : 
                    j += 1 
                elif(result > 0) : 
                    k -= 1 
                else : 
                    ans.append([nums[i],nums[j],nums[k]]) 
                    j += 1 
                    k -= 1 
                    while(j < k and nums[j] == nums[j-1]) : 
                        j += 1 
                    while(j < k and nums[k] == nums[k+1]) : 
                        k -= 1 
        return ans
                


class Solution:
     def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  
        arr = [] 
        # first k lae naya array ma store
        for i in range(n-k,n) :  
            arr.append(nums[i]) 
        # then rotate gareko pugni samma 
        for i in range(n-k-1,-1,-1) : 
            nums[i+k] = nums[i] 
        # tespaxi adding the array element laskarai 
        for i in range(k) : 
            nums[i] = arr[i] 
         
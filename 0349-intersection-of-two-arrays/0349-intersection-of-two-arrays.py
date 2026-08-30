class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []  
        for nums in nums1 : 
            if nums in nums2 and nums not in arr: 
                arr.append(nums) 

        return arr
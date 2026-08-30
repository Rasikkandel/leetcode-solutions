class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1) 
        n = len(nums2) 
        total = m + n 
        median_idx = total // 2 
        i = j = idx = 0 
        prev = current = 0 

        while idx <= median_idx : 
            if i < m and (  j >= n or nums1[i] < nums2[j]) : 
                prev , current = current , nums1[i] 
                i += 1 
            else : 
                prev , current = current , nums2[j] 
                j += 1 
            idx += 1 
        
        if total % 2 : 
            return float(current) 
        
        return (current + prev) / 2
            
            
        
        



        
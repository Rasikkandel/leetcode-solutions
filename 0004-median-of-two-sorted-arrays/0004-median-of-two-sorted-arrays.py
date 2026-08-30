class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1) 
        n = len(nums2) 
        median_idx = (m+n) // 2 
        i = 0 
        j = 0 
        idx = 0 
        median = 0 
        bhettiyo = 0 
        temp = [] 
        while(i < m and j < n) : 
            if(nums1[i] < nums2[j]) :
                temp.append(nums1[i])  
                if(idx == median_idx) : 
                    bhettiyo = 1 
                    break 
                idx += 1 
                i += 1

            else : 
                temp.append(nums2[j]) 
                if(idx == median_idx) : 
                    bhettiyo = 1
                    break 
                idx += 1  
                j += 1 
        
        while(i < m and bhettiyo == 0 ) : 
            temp.append(nums1[i])  
            if(idx == median_idx) : 
                break 
            idx += 1 
            i += 1
        
        while(j < n and bhettiyo == 0) : 
            temp.append(nums2[j])  
            if(idx == median_idx) : 
                break 
            idx += 1 
            j += 1


        if((m+n)%2 != 0) : 
            return temp[-1]
        else : 
            return (temp[-1] + temp[-2]) / 2
            
            
        
        



        
class Solution:
    def merge(self , arr , low , mid , high) : 
        left = low 
        right = mid + 1 
        temp = [] 
        while(left <= mid and right <= high) : 
            if(arr[left] < arr[right]) : 
                temp.append(arr[left]) 
                left += 1 
            else : 
                temp.append(arr[right]) 
                right += 1 
        while(left <= mid) : 
            temp.append(arr[left]) 
            left += 1 
        while(right <= high) : 
            temp.append(arr[right]) 
            right += 1 
        for i in range(len(temp)) : 
            arr[low+i] = temp[i]  
         
    def countpairs(self , arr , low , mid , high) -> int: 
        count = 0 
        right = mid + 1 
        for i in range(low , mid+1) : 
            while(right <= high and arr[i] > 2 * arr[right]) : 
                right += 1 
            count += right - (mid + 1)
        return count                 
                 

    def mergesort(self , arr , low , high) -> int :
        cnt = 0  
        if(low >= high) : 
            return cnt 
        mid = (low + high) // 2 
        cnt += self.mergesort(arr, low , mid) 
        cnt += self.mergesort(arr , mid+1 , high) 
        cnt +=  self.countpairs(arr , low , mid , high)
        self.merge(arr , low , mid , high ) 
        return cnt 

    def reversePairs(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 1
        cnt = self.mergesort(nums , low , high)
        return cnt 


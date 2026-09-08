class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_dict = {} 
        ans_list = [] 
        min_count = len(nums) // 3 
        for i in nums : 
            if(i in count_dict) : 
                count_dict[i] += 1
                continue 
            count_dict[i] = 1 
        for key in count_dict : 
            if(count_dict[key] > min_count) : 
                ans_list.append(key) 
        return ans_list
        

        
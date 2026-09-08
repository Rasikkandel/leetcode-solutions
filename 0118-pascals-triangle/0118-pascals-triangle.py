class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans_list = [] 
        for i in range(1,numRows+1) : 
            templist = [1] 
            ans = 1 
            for j in range(1,i) : 
                ans = ans * (i-j) 
                ans = ans / j  
                templist.append(int(ans))  
            ans_list.append(templist) 
        return ans_list
            

        
        
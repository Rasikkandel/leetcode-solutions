class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = [] 
        for i in range(left,right+1) : 
            if i < 10 : 
                ans.append(i) 
                continue
            org = i 
            while(org > 0) : 
                remainder = org % 10 
                org = org // 10 
                if remainder == 0 or i % remainder != 0 : 
                    break 
            else : # else runs when loop doesnt break
                ans.append(i) 
        return ans
                 
        
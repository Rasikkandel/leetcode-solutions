class Solution:
    def fact(self, n : int) -> int : 
        if n == 0 or n == 1 : 
            return 1 
        return n * self.fact(n-1) 
    def getRow(self, rowIndex: int) -> list[int]:
        ans = [] 
        nfact = self.fact(rowIndex) 
        print(nfact)
        for i in range(rowIndex+1) : 
            combination = nfact // (self.fact(rowIndex-i) * self.fact(i)) 
            ans.append(combination)
        return ans 


        
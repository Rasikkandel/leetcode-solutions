class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits) 
        count = 0 
        unique = set() 
        for i in range(n) : 
            if digits[i] == 0 : 
                continue
            for j in range(n) : 
                if i == j : 
                    continue 
                for k in range(n) : 
                    if i == k or j == k or digits[k] % 2 != 0: 
                        continue 
                    number = digits[i]*100 + digits[j]*10 + digits[k] 
                    if number not in unique : 
                        unique.add(number) 
                        count += 1
                      
        return count 










            


        
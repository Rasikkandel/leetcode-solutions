class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits) 
        count = 0 
        unique = set() 
        for i in range(n) : 
            for j in range(n) : 
                for k in range(n) : 
                    if j != i and k != j and i != k: 
                        if digits[i] != 0 : 
                            num = [digits[i] , digits[j] , digits[k] ] 
                            number = int("".join(map(str, num)))  
                            if number % 2 == 0 and number not in unique: 
                                count += 1 
                                unique.add(number)
                            
        return count








            


        
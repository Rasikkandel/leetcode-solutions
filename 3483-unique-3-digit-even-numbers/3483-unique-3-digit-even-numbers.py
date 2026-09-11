"""
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
        """
from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = Counter(digits)
        total = 0
        for h in range(1, 10):       
            if cnt[h] == 0:
                continue
            for t in range(10):      
                if cnt[t] == 0:
                    continue
                for u in (0, 2, 4, 6, 8): 
                    if cnt[u] == 0:
                        continue
                    need = Counter((h, t, u))
                    if all(cnt[d] >= c for d, c in need.items()):
                        total += 1
        return total










            


        
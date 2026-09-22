class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        k -= 1  
        result = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            idx = k // f
            k %= f
            result.append(str(numbers.pop(idx)))
        return "".join(result)
            



            


        
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0 
        primitives = [] 
        primitive = ""
        for character in s: 
            primitive += character 
            if character == "(" : 
                count += 1 
            elif character == ")" : 
                count -= 1 
            if count == 0 : 
                primitives.append(primitive)
                primitive = ""
        ans = ""
        for prim in primitives : 
            ans += prim[1:-1] 
        return ans
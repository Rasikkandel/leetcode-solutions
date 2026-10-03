class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0 
        ans = ""
        primitive = ""
        for character in s: 
            primitive += character 
            if character == "(" : 
                count += 1 
            elif character == ")" : 
                count -= 1 
            if count == 0 : 
                ans += primitive[1:-1] 
                primitive = ""
        return ans
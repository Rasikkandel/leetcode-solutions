class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ## naive approach 
        """
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
        """ 
        # optimal approach 
        depth = 0 
        ans = [] 
        for character in s : 
            if character == "(" : 
                if depth > 0 : 
                    ans.append(character) 
                depth += 1 
            else : 
                depth -= 1 
                if depth > 0 : 
                    ans.append(character) 
        return "".join(ans)

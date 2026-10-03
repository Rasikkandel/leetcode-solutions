class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0 
        max_depth = 0 
        for character in s : 
            if character == "(" : 
                depth += 1 
                max_depth = max(max_depth , depth)
            elif character == ")" : 
                depth -= 1 
        return max_depth
        
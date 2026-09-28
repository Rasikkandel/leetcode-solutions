class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0 
        max_count = 0 
        for character in s : 
            if character == "(" : 
                count += 1 
                max_count = max(max_count , count)
            elif character == ")" : 
                count -= 1 
        return max_count
        
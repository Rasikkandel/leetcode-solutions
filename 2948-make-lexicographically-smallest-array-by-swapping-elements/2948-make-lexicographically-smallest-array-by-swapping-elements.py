class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])
        result = [0] * n

        i = 0
        while i < n:
            j = i 
            group = [order[i]]
            while j + 1 < n and nums[order[j + 1]] - nums[order[j]] <= limit:
                j += 1
                group.append(order[j])

            for pos, val in zip(sorted(group), sorted(nums[k] for k in group)):
                result[pos] = val

            i = j + 1

        return result 
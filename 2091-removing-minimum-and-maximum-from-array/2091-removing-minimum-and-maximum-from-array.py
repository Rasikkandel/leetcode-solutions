class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = 0   # index of the smallest element seen so far
        max_index = 0   # index of the largest element seen so far

        # Single pass to find where the min and max values are located
        for i in range(n):
            if nums[i] > nums[max_index]:
                max_index = i
            if nums[i] < nums[min_index]:
                min_index = i

        # We need to remove both the min and max element.
        # It doesn't matter which one is which — what matters is which
        # one comes FIRST (earlier index) and which comes LAST (later index),
        # since deletions always happen from the front and/or back of the array.
        earlier_index = min(min_index, max_index)   # whichever of min/max appears first
        later_index = max(min_index, max_index)     # whichever of min/max appears last

        # There are exactly 3 possible strategies — try all, take the cheapest:

        # 1) Delete everything from the FRONT up through later_index.
        #    This removes both min and max in one prefix deletion.
        delete_prefix_only = later_index + 1

        # 2) Delete everything from the BACK starting at earlier_index.
        #    This removes both min and max in one suffix deletion.
        delete_suffix_only = n - earlier_index

        # 3) Delete a prefix up through earlier_index AND a suffix from later_index onward.
        #    Useful when min and max are far apart near opposite ends —
        #    cheaper to trim both sides a little than to remove one huge chunk.
        delete_both_ends = (earlier_index + 1) + (n - later_index)

        return min(delete_prefix_only, delete_suffix_only, delete_both_ends)
     
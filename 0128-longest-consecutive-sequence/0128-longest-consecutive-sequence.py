class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Runtime beats 90.3%
        ## Memory beats 86.81%
        num_set = set(nums) # O(n) build, O(1) lookup
        best = 0
        for num in num_set:
            # Only start counting from the beginning of a sequence
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                best = max(best, length)

        return best

        """
        ## Runtime beats 98.67
        ## Memory beats 66.67%
        if not nums: return 0 
        nums = sorted(set(nums)) # dedupe + sort; O(n log n)
        best = curr = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                curr = 1
            best = max(best, curr)
        return best
        """


        
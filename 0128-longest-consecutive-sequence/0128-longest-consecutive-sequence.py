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

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([100,4,200,1,3,2],4),
        ([0,3,7,2,5,8,4,6,0,1],9),
        ([1,0,1,2],3),
        ([5,5,5,5],1),
        ([1,2,2,3,3,3,4,4,4,4],4),
        ([-5,-4,5,-3,-2,8,-1,9,0,1,5,8,9],7),
        ([10],1),
        ([9,8,7,12,14,15,16,17,19,21,-20,20,-22,18],8)
    ]

    for nums,expected in test_cases:
        output = sol.longestConsecutive(nums)
        status = "✅ PASS " if output == expected else "❌ FAIL"
        print(f"{status} | nums={nums} => {output}")
        
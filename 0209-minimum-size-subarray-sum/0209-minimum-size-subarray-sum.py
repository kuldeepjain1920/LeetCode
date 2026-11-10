class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        n = len(nums)
        min_length = n+1

        ## keep including/expanding the right element from left -> right
        ## till the target sum is reached
        for right in range(len(nums)):
            current_sum += nums[right]

            ## Shrink the left element as soon as target sum is reached
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length <= n else 0

        
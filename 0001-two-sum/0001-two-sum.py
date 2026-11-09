class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime beats 5.00% - bad
        Memory beats 82.5% - good
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    return [i,j]
        return None
        """


        ### Runtime beats 40.6%
        ### Memory beats 18.18%
        seen = {} ## value and index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index
    
        
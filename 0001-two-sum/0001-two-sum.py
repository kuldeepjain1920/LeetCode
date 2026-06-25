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
    map = {} ## value and index
    for index, num in enumerate(nums):
        diff = target - num
        if diff in map:
            return [map[diff], index]
        map[num] = index
    return None
    """
    index = 0
    for num in nums:
        diff = target-num
        try:
            otherIndex = nums.index(diff,index+1)
        except ValueError:
            otherIndex = -1
        if otherIndex >= 0:
            return [index, otherIndex]
        index += 1
    return None
    """

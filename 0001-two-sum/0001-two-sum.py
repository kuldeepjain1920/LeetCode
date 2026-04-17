class Solution:
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        parsedNum = {} ## value and index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in parsedNum:
                return [parsedNum[diff], index]
            parsedNum[num] = index
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
    """




        
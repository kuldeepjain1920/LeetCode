class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ##return len(set(nums)) != len(nums)
        nMap = {}
        for i in range(len(nums)):
            nMap[nums[i]] = nMap.get(nums[i], 0) + 1
            if nMap.get(nums[i]) > 1:
                return True
        return False
        
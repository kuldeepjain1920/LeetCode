class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ##return len(set(nums)) != len(nums)
        nMap = {}
        for i in range(len(nums)):
            cnt = nMap.get(nums[i], 0)
            if cnt > 0:
                return True;
            nMap[nums[i]] = cnt + 1
            """
            nMap[nums[i]] = nMap.get(nums[i], 0) + 1
            if nMap.get(nums[i]) > 1:
                return True
            """
        return False
        
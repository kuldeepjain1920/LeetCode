class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = [1] * n

        ## Best Approach extra space O(1), 
        ## result is output and is not consider as extra space
        ## Runtime beats 75.85%
        ## Memory beats 70.55%
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

        """
        ## using 3 arrays and O(n) extra space
        ## Runtime beats 31.8%
        ## Memory beats 14.18%
        prefix = [1]*n
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1]*n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        result = [prefix[i] * suffix[i] for i in range(n)]

        return result
        """
        """
        ## Time Limit Exceeded O(N²)
        return [
            math.prod(nums[:i] + nums[i+1:]) for i in range(n)
        ]
        """

## ✅ Test block OUTSIDE the class
if __name__ == "__main__":
    
    sol = Solution()

    test_cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        ([0,0,3,4], [0,0,0,0]),
        ([-1, 2, -3, 4], [-24,12,-8,6]),
        ([3,5], [5,3])
    ]

    for nums, expected in test_cases:
        output = sol.productExceptSelf(nums)
        status = "✅ PASS" if output == expected else " ❌ FAIL"
        print(f"{status} | nums={nums} => {output}")
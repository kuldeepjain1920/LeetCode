class Solution:
    def trap(self, height: List[int]) -> int:
        """
        ## Two pointers Time:O(N), Space O(1)
        ## Runtime 7 ms Beats 74.4%
        water = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0

        while left < right:
            if height[left] < height[right]:
                # Right side is taller, left_max is true constraint
                if height[left] >= left_max:
                    left_max = height[left] ## new left wall, no water here
                else:
                    water += left_max - height[left]
                left += 1
            else:
                # Left side is taller, right_max is true constraint
                if height[right] >= right_max:
                    right_max = height[right] # new right wall, no water here
                else:
                    water += right_max - height[right]
                right -= 1

        return water
        """
        ## Approach 2
        ## PREFIX-MAX ARRAYS Time:O(N) Space O(N)
        ## 
        n = len(height)
        if n == 0: return 0
        left_max = [0] * n ## left_max[i] = max_height from 0..i
        right_max = [0] * n ## right_max[i] = max_height from i..n-1

        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        return sum(
            min(left_max[i], right_max[i]) - height[i] for i in range(n)
        )

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1],6),
        ([4,2,0,3,2,5],9),
        ([5],0),
        ([],0),
        ([3,4],0),
        ([3,0,0,0,4],9),
        ([1,2,3,4,5],0),
        ([0,1,0,2,0,1,0],2),
        ([0,0,0,0,0,0],0)
    ]

    for nums, expected in test_cases:
        output = sol.trap(nums)
        status = "✅ PASS" if output == expected else "❌ FAIL"
        print(f"{status} | nums={nums} => {output}")


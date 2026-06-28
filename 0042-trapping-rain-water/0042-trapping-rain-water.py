class Solution:
    def trap(self, height: List[int]) -> int:
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


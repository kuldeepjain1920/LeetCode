class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        ## My version
        ## Runtime beats 92.11
        ## Memory beats 37.18%
        left = 0
        right = len(height) - 1
        area = 0
        while left <= right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return area
        """

        ## Cleaner and more readable code
        ## Runtime beats 52.08%
        ## Memory beats 37.18%
        left, right = 0, len(height) - 1
        max_area = 0

        while left <= right:
            width = right - left
            area = width * min( height[left], height[right])
            max_area = max(max_area, area)

            #Move the SHORTER pointer inwards
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,8,6,2,5,4,8,3,7],49),
        ([1,1],1),
        ([5,5,5,5,5,5,5,5,5], 40),
        ([1,2,3,4,5],6),
        ([6,5,4,3,2,1],9),
        ([1,1,1,10,1,1,1],6),
        ([10,1,1,1,1,1,10],60)
    ]
    
    for nums, expected in test_cases:
        output = sol.maxArea(nums)
        status = "✅ PASS" if output == expected else "❌ FAIL"
        print(f"{status} | nums={nums} => {output}")

        
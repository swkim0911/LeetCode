class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volumn = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volumn += left_max - height[left]
                left += 1

            else:
                volumn += right_max - height[right]
                right -= 1

        return volumn
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volumn = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right] # 초기값
        while left < right:
            if height[left] <= height[right]:
                left_max = max(height[left], left_max)
                volumn += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                volumn += right_max - height[right]
                right -= 1

        return volumn
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # [left: right + 1]

        
        while left <= right:
            mid = (left + right) // 2 # mid: nums 배열 안에서 search되는 index
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        return -1


# 문제 정의: target 정수가 nums배열에 있는지 찾고, 있으면 index를, 없으면 -1을 리턴해야 한다. 단, 시간복잡도는 O(logn)
# 해결: 시간복잡도 요구를 만족하기 위해서 linear search가 아닌 binary search를 해야 한다.

        
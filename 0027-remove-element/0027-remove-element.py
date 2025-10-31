class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# 정의: in-place, 즉 배열을 새로 생성하지 않고 val과 같은 값을 nums 배열에서 삭제해야 한다.
# 해결책: 새로운 배열을 생성하지 않고, val과 같은 값을 생성하기 위해서는 
# 배열 안에 val과 다른 값을 저장할 위치를 참고할 수 있는 i, 그리고 linear하게 탐색할 j 변수가 필요하다.
# nums 배열을 탐색하면서 val과 다른 값

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = -1
        for j in range(0, len(nums)):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
        return i + 1


# i,j 
# 둘다 아니면 i+1, j+1
# i는 아니고, j는 맞으면 j가 아닌거 찾을때까지 앞으로
# 찾으면 i+1하고 i+1 위치랑 j위치 교환

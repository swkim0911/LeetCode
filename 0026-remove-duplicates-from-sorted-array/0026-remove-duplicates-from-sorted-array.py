class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        # 0 1 1 1 2 3 4
        # 

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1 # 다른게 나오면 현재 위치(i) 앞에 다른 수를 놓기
                nums[i] = nums[j]
            # 같다면 어디까지 다른게 나올지 확인
        
        
        
        return i + 1

# 문제 조건: in-place (메모리를 새로 할당하지 않고) 중복 제거하고 정렬 상태 유지하기. 그리고 중복하지 않는 값의 크기 (k) 반환하기



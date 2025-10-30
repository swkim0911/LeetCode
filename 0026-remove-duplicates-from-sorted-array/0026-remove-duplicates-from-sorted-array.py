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
# in-place로 문제를 풀어야 하기 때문에 두 개의 포인터로 배열을 탐색합니다.
# i,j 변수른 선언하고 선형 탐색을 하면서 nums[i] == nums[j] 라면 중복되지 않는 때를 찾기 위해 j++를 하며 탐색합니다.
# nums[i] != nums[j]가 나온다면 i 중복이 끝나고 다른 정수를 만난거니까 다음 위치 (i+1)에 nums[j]를 두면서 정렬 순서를 유지하면서 중복된 정수를 없앱니다.


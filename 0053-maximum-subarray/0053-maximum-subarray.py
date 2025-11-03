class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def find_max_subarray(nums, left, right):
            # 기저 조건: 하나의 원소만 남았을 때
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2

            # 왼쪽, 오른쪽, 중앙을 가로지르는 최대 부분합 계산
            left_max = find_max_subarray(nums, left, mid)
            right_max = find_max_subarray(nums, mid + 1, right)
            cross_max = find_cross_sum(nums, left, mid, right)

            # 세 경우 중 최댓값 반환
            return max(left_max, right_max, cross_max)

        def find_cross_sum(nums, left, mid, right):
            # 왼쪽 끝부분에서 mid까지의 최대 부분합
            left_sum = float('-inf')
            cur = 0
            for i in range(mid, left - 1, -1):  # mid → left 방향으로 이동
                cur += nums[i]
                left_sum = max(left_sum, cur)

            # 오른쪽 시작부분에서 mid+1 → right까지의 최대 부분합
            right_sum = float('-inf')
            cur = 0
            for i in range(mid + 1, right + 1):  # mid+1 → right 방향으로 이동
                cur += nums[i]
                right_sum = max(right_sum, cur)

            # 중앙을 가로지르는 합 = 왼쪽 + 오른쪽
            return left_sum + right_sum

        # 초기 호출
        return find_max_subarray(nums, 0, len(nums) - 1)

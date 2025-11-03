# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        # [1,2,3,4,5]
        while left < right: # 왼쪽의 True 찾기
            mid = (left + right) // 2
            if(isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        return right

# 문제 정의: isBadVersion API를 호출했을 때 처음으로 bad version이 되는 버전의 위에 버전 찾기
# 해결: n의 크기가 2^31 - 1 (21억 개) 가 되니까 O(n)으로 탐색하면 시간 초과가 발생할 수 있다.
# 그래서 이분 탐색으로 문제에서 요구하는 지점을 찾으면 O(logn)의 시간복잡도로 찾을 수 있다.

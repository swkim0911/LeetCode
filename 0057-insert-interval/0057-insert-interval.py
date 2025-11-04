class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1: newInterval 보다 뒤에 있는 구간 처리
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # 2: newInterval과 겹치는 구간 처리
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)
        
        # 3: newInterval 보다 앞에 있는 구간 처리
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

# 문제 정의: 정렬된 intervals 배열에 newInterval 의 구간을 반영해서, 오름차순 정렬된 상태, interval들의 범위가 겹치지지 않는 상태를 유지해야 한다.

# 브루트포스: 직관적으로 10_001 크기의 배열을 선언하고 interval 구간을 직접 표시한 다음에 거기에 newInterval을 반영할 수 있지만 이러면 10억 번 연산을 해야 해서 timeout이 발생할 수 있다.

# 시간 복잡도: O(n)
# 공간 복잡도: O(n)
# 풀이: intervals 배열을 순회하면서 newInterval보다 뒤에 있는 구간은 result에 그대로 추가한다.
# 이후에 newInterval 구간과 겹치는 interval 구간이 발생하면 newInterval 구간에 겹치는 구간을 반영한다.
# 이때 겹치는 걸 판단하는 조건은 !(interval.end < newInterval.start) 이 된다.
# 이렇게 정할 수 있는 이유는 오름차순으로 intervals 배열을 순회해서 앞쪽에 겹치지 않는 조건인 newInterval < interval.start 을 수행했기 때문이다.
# 겹치는 부분을 처리 끝내고 나머지 newInterval보다 앞에 있는 interval을 result에 그대로 추가하면 된다.

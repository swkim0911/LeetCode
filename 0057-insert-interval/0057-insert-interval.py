class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        idxs = []

        for i, interval in enumerate(intervals):
            start, end = interval
            if end < newInterval[0] or start > newInterval[1]:
                continue
            idxs.append(i)

        if not idxs:
            intervals.append(newInterval)
            return sorted(intervals, key= lambda x: x[0])
            
        a = min(intervals[idxs[0]][0], newInterval[0])
        b = max(intervals[idxs[-1]][1], newInterval[1])
        result_interval = [a, b]
        answer = []
        flag = False
        for i in range(len(intervals)):
            if i not in idxs:
                answer.append(intervals[i])
            else:
                if not flag:
                    answer.append(result_interval)
                    flag = True
        
        return answer

            

# 구간과 구간에 대해서 가능한 관계는 총 6가지



# 문제 정의: 정렬된 intervals 배열에 newInterval 의 구간을 반영해서, 오름차순 정렬된 상태, interval들의 범위가 겹치지지 않는 상태를 유지해야 한다.
# 직관적으로 10_001 크기의 배열을 선언하고 interval 구간을 직접 표시한 다음에 거기에 newInterval을 반영할 수 있지만 이러면 
# 10억 번 연산을 해야 해서 timeout이 발생할 수 있다.
#  
# 풀이: 

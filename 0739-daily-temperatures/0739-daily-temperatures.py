class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stack에 계속 쌓인다는 것은 나보다 더 높은 온도를 만나지 못한것
        result = [0] * len(temperatures)
        
        for i, cur in enumerate(temperatures):
            
            # 현재 내가 stack의 맨 위 날씨 보다 낮다면 stack에 있는 모든 날씨보다 내가 낮을 수 밖에 없다.
            # 그래서 스택의 맨 위만 확인해도 된다.
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            
            stack.append(i) # 인덱스를 저장함으로써 인덱스 차이로 몇 일만에 높은 온도가 왔는지 알 수 있다.
        
        return result
        
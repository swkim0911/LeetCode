class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (46) # dp[x]: 1과 2로 x steps까지 가는 총 경우의 수
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        

# 문제 정의: 1과 2로만 구성해서 n까지 가는데 서로 다른 경우가 몇 가지가 있는지 구해야 한다.
# 해결: DP로 풀 수 있다. 점화식을 dp[x] = dp[x - 1] + dp[x - 2] 로 정의할 수 있는데
# dp[x - 1] + dp[x - 2] 에서 dp[x - 1] 은 x-1 steps를 만들 수 있는 모든 경우에 1 step을 더한 경우이고
# dp[x - 2] 은 x-2 steps를 만들 수 있는 모든 경우에 2 step을 더한 경우이다.
# 이렇게 더하면 dp[x-1]에서 만드는 경우와 dp[x-2]에서 만드는 경우가 겹치지 않기 때문에 dp[x]를 구할 수 있다.

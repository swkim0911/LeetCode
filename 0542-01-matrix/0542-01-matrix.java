import java.util.*;

class Solution {

    static final int INF = Integer.MAX_VALUE / 2;

    public int[][] updateMatrix(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int[][] dp = new int[n][m]; // 현재 위치(1)에서 0까지 거리 중 최소 거리

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(mat[i][j] != 0){
                    dp[i][j] = INF;
                }
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(dp[i][j] > 0){
                    if(i > 0) dp[i][j] = Math.min(dp[i][j], dp[i-1][j] + 1);
                    if(j > 0) dp[i][j] = Math.min(dp[i][j], dp[i][j-1] + 1);
                }
            }
        }
        for(int i = n-1; i >= 0; i--){
            for(int j = m-1; j >= 0; j--){
                if(dp[i][j] > 0){
                    if(i < n - 1) dp[i][j] = Math.min(dp[i][j], dp[i+1][j] + 1);
                    if(j < m - 1) dp[i][j] = Math.min(dp[i][j], dp[i][j+1] + 1);
                }
            }
        }

        return dp;
    }

}


// 문제 정의: 각 셀에 대해서 가장 가까운 0과의 거리 찾기
// 해결: 
// 처음에는 bfs로 0이 아닌 cell에서 bfs로 가장 가까이에 있는 0의 거리를 찾는다.
// 이렇게 하면 timeout이 발생한다.
// 시간 복잡도: O((n*m)*(n*m)) -> timeout
// 그래서 DP로 이전 경우를 기록한다면 시간복잡도를 줄일 수 있다.
// dp[x][y]: (x,y) 위치에서 0까지 최단 거리라고 정의하면 점화식은
// dp[x][y] = Math.min(dp[x][y], dp[x-1][y], dp[x][y-1], dp[x+1][y], dp[x][y+1]) 로 정의할 수 있다.
// 이때, 이 점화식은 한 번에 계산할 수 없는데 이유는 dp[x-1][y], dp[x][y-1]은 왼쪽 위에서 내려오면서 최단 거리를 갱신하고, dp[x+1][y], dp[x][y+1]은 오른쪽 아래에서 올라가면서 최단 거리가 갱신되기 떄문에, 따로 나누어서 최단 거리를 갱신해야 한다.

// 시간 복잡도: O(n*m)
// 공간 복잡도: O(n*m)
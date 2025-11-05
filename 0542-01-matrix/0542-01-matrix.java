import java.util.*;

class Solution {

    int[] dx = {-1,0,1,0};
    int[] dy = {0,-1,0,1};
    static final int INF = Integer.MAX_VALUE;

    public int[][] updateMatrix(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int[][] dist = new int[n][m]; // 0에서 최소 거리
        for(int i = 0; i < n; i++){
            Arrays.fill(dist[i], INF); // INF으로 초기화
        }
        
        Queue<Point> q = new LinkedList<>();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(mat[i][j] == 0){
                    q.add(new Point(i,j));
                    dist[i][j] = 0;
                }
            }
        }
        while(!q.isEmpty()){
            Point cur = q.poll();

            for(int i = 0; i < 4; i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if(dist[nx][ny] > dist[cur.x][cur.y] + 1){
                    dist[nx][ny] = dist[cur.x][cur.y] + 1;
                    q.add(new Point(nx,ny));
                }
            }
        }

        return dist;
    }

}

class Point{
    int x,y;

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}
// 문제 정의: 각 셀에 대해서 가장 가까운 0과의 거리 찾기
// 해결: 0 에게 가장 가까운 건 자기자신이니까 0.
// bfs로 0이 아닌 cell에서 bfs로 가장 가까이에 있는 0의 거리를 찾는다.
// bfs 특성상 큐를 사용하기 때문에 순회를 하면서 가장 먼저 찾은 0일 때, 그때가 최소 거리이다.
// mat 배열에 0이 아닌 값은 모두 -1로 초기화한 다음에 -1은 아직 최소 거리를 찾지 않는 셀, 정수 > 0는 이미 찾은 셀로 구분한다.
// 시간 복잡도: O((n*m)*(n*m)) -> timeout
// 모든 셀을 방문해서 조회하면 timeout이 발생하니까 dp로 해결할 수 있다.

// dp의 정수 값만으로 
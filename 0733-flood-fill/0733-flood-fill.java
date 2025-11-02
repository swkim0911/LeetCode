class Solution {

    int[] dx = {-1,0,1,0};
    int[] dy = {0,-1,0,1};

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        bfs(image, new Point(sr,sc), image[sr][sc], color);

        return image;
    }

    public void bfs(int[][] image, Point start, int origin, int color){
        int n = image.length;
        int m = image[0].length;
        boolean[][] visited = new boolean[n][m];

        Queue<Point> q = new LinkedList<>();
        q.add(start);
        visited[start.x][start.y] = true;

        while(!q.isEmpty()){
            Point cur = q.poll();
            image[cur.x][cur.y] = color;

            for(int i = 0; i < 4; i++){
                int nx = dx[i] + cur.x;
                int ny = dy[i] + cur.y;
                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위를 벗어난 경우
                if(visited[nx][ny]) continue; // 이미 방문한 경우
                if(image[nx][ny] != origin) continue;
                visited[nx][ny] = true;
                q.add(new Point(nx,ny));
            }
        }
    }
}

class Point{
    int x,y;

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}
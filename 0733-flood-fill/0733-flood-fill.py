from collections import deque

class Solution:

    def dfs(self, image: List[List[int]], sr: int, sc: int, origin: int, color: int) -> None:
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]

        n = len(image)
        m = len(image[0])

        dq = deque([])
        dq.append((sr,sc))
        visited = [[False] * m for _ in range(n)] # 방문 여부 체크 이차원 배열
        visited[sr][sc] = True

        while dq:
            cur_x, cur_y = dq.popleft()
            image[cur_x][cur_y] = color

            for i in range(4):
                nx = dx[i] + cur_x
                ny = dy[i] + cur_y

                if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위를 벗어나는 경우
                    continue
                if visited[nx][ny]: # 이미 방문한 경우
                    continue
                if image[nx][ny] != origin: continue # 출발점과 색이 다른 경우
                
                visited[nx][ny] = True
                dq.append((nx,ny))






    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr, sc, image[sr][sc], color)
        return image
        
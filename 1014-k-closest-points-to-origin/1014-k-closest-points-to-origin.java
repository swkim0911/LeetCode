import java.util.*;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // 1. 정렬
        Arrays.sort(points, (o1,o2) -> (o1[0] * o1[0] + o1[1] * o1[1]) - (o2[0] * o2[0] + o2[1] * o2[1]));
        int[][] answer = new int[k][2];
        for(int i = 0; i < k; i++){
            answer[i][0] = points[i][0];
            answer[i][1] = points[i][1];
        }

        return answer;
    }
}

// 문제 정의: points 배열이 주어졌을 때, 원점(0,0)에 가장 가까운 점, k 개를 반환한다. 단, 어떤 순서든 상관이 없다.
// 문제 해결: points 배열을 순회하면서
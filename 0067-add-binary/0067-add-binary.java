class Solution {
    public String addBinary(String a, String b) {
        String answer = "";
        int aIdx = a.length() - 1;
        int bIdx = b.length() - 1;
        int before = 0;
        while(aIdx >= 0 || bIdx >= 0){
            int aVal = aIdx >= 0 ? a.charAt(aIdx) - '0' : 0;
            int bVal = bIdx >= 0 ? b.charAt(bIdx) - '0' : 0;
            
            if(aVal + bVal + before < 2){ // 0 혹은 1
                answer = String.valueOf(aVal + bVal + before) + answer;
                before = 0;
            }else{ // 2 이상인 경우
                answer = String.valueOf(aVal + bVal + before - 2) + answer;
                before = 1;
            }
            aIdx -= 1;
            bIdx -= 1;
        }
        if(before > 0){
            answer = "1" + answer;
        }

        return answer;
    }
}
// 문제 정의: 두 이진수를 표현하는 문자열 a,b가 있을 때, 두 값의 합을 문자열로 리턴한다.
// 풀이: 실제로 덧셈 연산을 하는 것처럼 푼다. a,b의 첫번째 자리 index(aIdx, bIdx)를 시작으로 각 위치의 값을 더하면서 넘어가는 수(before)을 기록하면서 str 문자열에 결과값을 붙인다.
// 모두 끝났을 때 넘어가는 수가 1 남아 있으면 마지막으로 1 + str을 처리한다.
// 시간 복잡도: O(n)
// 공간 복잡도: answer += str 부분에서 문자열을 계속 생성해서 O(n^2) 공간이 필요하다.

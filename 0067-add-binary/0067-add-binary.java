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
// 풀이: 1) a를 정수로 바꾸고, b를 정수로 바꾼 다음 서로 더한 다음에 다시 문자열로 변경
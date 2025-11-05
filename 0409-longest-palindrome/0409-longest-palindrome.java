import java.util.*;

class Solution {
    public int longestPalindrome(String s) {
        int answer = 0;
        HashMap<Character, Integer> charCntMap = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            charCntMap.put(c, charCntMap.getOrDefault(c, 0) + 1);
        }
        boolean hasOdd = false;

        for(Map.Entry<Character, Integer> entry : charCntMap.entrySet()){
            int cnt = entry.getValue();
            if(cnt % 2 == 0){
                answer += cnt;
            }else{
                answer += (cnt - 1);
                hasOdd = true;
            }
        }
        if(hasOdd) answer += 1;

        return answer;
    }
}
// 문제 정의: 주어진 문자열의 문자들로 가장 긴 팰린드롬을 만들기
// 해결: 문자의 개수가 짝수이면 팰린드롬을 만드는데 모두 사용하면 된다.
// 문자의 개수가 홀수이면 이 중에서 짝수 개수만 사용하면 돼서 cnt - 1을 더하면 된다.
// 마지막에 개수가 홀수인 문자로 팰린드롬을 만들었다면 그 문자의 한 개는 가운데 놓아서 최대 크기를 만들 수 있다. 

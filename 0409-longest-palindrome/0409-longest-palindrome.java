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
// 해결: 문자의 개수가 짝수이면 팰린드롬을 만드는데 항상 사용할 수 있다.

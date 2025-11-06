import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> numToCntMap = new HashMap<>();
        for(int num : nums){
            numToCntMap.put(num,  numToCntMap.getOrDefault(num, 0) + 1);
        }
        int maxCnt = 0;
        int answer = 0;
        for(Map.Entry<Integer, Integer> entry : numToCntMap.entrySet()){
            if(maxCnt < entry.getValue()){
                answer = entry.getKey();
                maxCnt = entry.getValue();
            }
        }

        return answer;
    }
}

// 문제 정의: n 크기의 nums 배열이 주어졌을 때 majority element 요소를 찾는다. majority element는 그 원소의 개수가 절반보다 많은 원소이다.


import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        for(int num : nums){
            if(count == 0){
                candidate = num;
            }
            count += (candidate == num ? 1 : -1); 
        }

        return candidate;



    }
}

// 문제 정의: n 크기의 nums 배열이 주어졌을 때 majority element 요소를 찾는다. majority element는 그 원소의 개수가 절반보다 많은 원소이다.


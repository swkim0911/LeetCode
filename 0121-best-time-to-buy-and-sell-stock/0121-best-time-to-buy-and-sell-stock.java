
class Solution {
    public int maxProfit(int[] prices) {
        int minVal = Integer.MAX_VALUE;
        int maxProfit = 0;

        for(int price : prices){
            if(price < minVal){
                minVal = price;
            }else if(price - minVal > maxProfit){
                maxProfit = price - minVal;
            }
        }

        return maxProfit; 
    }
}
// 정의: 주식의 가격을 담은 배열이 주어졌을 때, 가장 큰 이윤값을 찾는 문제입니다. 즉, 낮은 가격에 사서 비싼 가격으로 팔 때, 가장 큰 gap을 찾아야 합니다.
// 풀이: 먼저 가장 쉽게 풀 수 있는 방법은 prices 배열의 모든 원소끼리 비교해서 가장 큰 이윤을 찾는겁니다. 하지만 prices 배열의 총 크기는 10만이고 시간복잡도가 O(N^2)로 100억번 연산해야 해서 시간초과가 발생할 수 있습니다.
// 그래서 다른 방법을 선택해야 하는데


// 


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# 문제 정의: t가 s의 애너그램인지 확인해야 한다.
# 풀아: 애너그램 관계는 두 문자열의 구성이 같다는 뜻이다. 
# 구성이 같다는 걸 확인하기 위해 문자열에 어떤 문자가 있고, 각 문자가 몇 개인지 구해서 둘이 같은지 (dict 혹은 Counter) 비교할 수 있지만
# 두 문자열을 정렬을 해서 같은 형태라면 두 문자열의 구성이 같다(애너그램)로 풀 수 있다.
# 정렬을 하면 O(nlogn) 이고, dict에 넣는다면 O(n) 이 된다.
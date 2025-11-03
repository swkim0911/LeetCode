from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = dict()
        
        for letter in magazine:
            if letter in m_dict:
                m_dict[letter] += 1
            else:
                m_dict[letter] = 1

        for letter in ransomNote:
            if letter not in m_dict:
                return False
            if m_dict[letter] <= 0:
                return False
            m_dict[letter] -= 1
        
        return True
# 문제 정의: magazine의 문자 집합으로 ransomNote 문자를 구성할 수 있는지 확인하는 문제이다.
# 해결: dict 자료 구조를 이용해서 magazine 문자열에 letter가 각각 몇 개 있지 count한다. 그리고 ransomNote의 문자를 순회하면서 m_dict에 대응하는 letter 키의 value를 -=1 하며 m_dict에 없거나 <= 0이 되면 magazine은 ransomNote를 만들지 못한다.
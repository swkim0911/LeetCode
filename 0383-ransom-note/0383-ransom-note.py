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
# 해결: dict 자료 구조를 이용해서 각 문자열의 letter가 몇 개인지 Count한다.
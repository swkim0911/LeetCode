from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_dict = Counter(ransomNote)
        m_dict = Counter(magazine)

        for letter, cnt in r_dict.items():
            if m_dict[letter] < cnt:
                return False
        
        return True
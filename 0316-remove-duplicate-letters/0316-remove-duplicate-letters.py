class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        if len(s) == 0:
            return ''
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))

        
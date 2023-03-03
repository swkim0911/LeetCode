class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 윈도우 안에 현재 char가 있는지 확인해야 하는데 확인할 때 윈도우 전체를 (loop를 돌면서) 보는게 아니라 used에 있고 start가 used[char]이전에 있음이 동치가 되어
            # 이 조건문으로 찾는다.
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
            
            # 현재 문자의 위치 삽입(문자가 이미 등장은 했어도 갱신을 해서 현재 윈도우에 있는 char의 index를 알아야 위에 if문이 제대로 동작한다)
            used[char] = index
        
        return max_length

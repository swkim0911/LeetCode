class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        collection = collections.Counter(s) # counter는 for문을 돌면서 앞으로 그 letter가 또 나올 수 있는지 count
        seen = set()
        stack = []

        for char in s:
            collection[char] -= 1

            if char in seen:
                continue
            
            # char가 stack 맨 위 문자보다 앞에 있고 stack 맨 위 문자가 나중에 더 나올 수 있다면 pop
            while stack and char < stack[-1] and collection[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)

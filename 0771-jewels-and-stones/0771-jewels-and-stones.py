class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = collections.defaultdict(int)
        result = 0

        for char in stones:
            dict[char] += 1

        for key in dict.keys():
            if key in jewels:
                result += dict.get(key)

        return result
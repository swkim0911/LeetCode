class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = collections.defaultdict(int)
        result = 0

        for char in stones:
            dict[char] += 1

        for jewel in jewels:
            if jewel in dict:
                result += dict[jewel]
                
        return result
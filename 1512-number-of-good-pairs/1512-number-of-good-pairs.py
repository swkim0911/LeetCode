class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = collections.Counter(nums)
        result = 0
        for key in dict:
            value = dict.get(key)
            if value > 1:
                result += self.combination(value)
        return result

    def combination(self, number: int):
        return number * (number - 1) // 2
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = collections.Counter(nums)
        result = []

        most_frequency = dict.most_common(k)
        for i, j in most_frequency:
            result.append(i)

        return result
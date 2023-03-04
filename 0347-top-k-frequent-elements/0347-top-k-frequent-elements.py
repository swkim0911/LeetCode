class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums);
        freqs_heap = []
        top_k = []

        # 빈도 수를 키로 하고, freqs의 key를 값으로 했다.
        # 파이썬의 힙은 최소 힙을 지원하기 때문에 음수를 붙힘.
        for key in freqs:
            heapq.heappush(freqs_heap, (-freqs[key], key))

        for _ in range(k):
            top_k.append(heapq.heappop(freqs_heap)[1]);
        return top_k
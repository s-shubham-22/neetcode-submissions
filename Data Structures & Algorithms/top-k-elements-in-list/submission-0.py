class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        freqMap = dict(sorted(freqMap.items(), key=lambda item: item[1], reverse=True))
        return list(freqMap)[:k]
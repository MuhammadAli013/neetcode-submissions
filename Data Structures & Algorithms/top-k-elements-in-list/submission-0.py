class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0)+1
        idxs = sorted(list(freq.values()),reverse=True)[:k]
        ks = []
        for f in freq:
            # print(freq[f])
            if freq[f] in idxs:
                ks.append(f)
        return ks
        
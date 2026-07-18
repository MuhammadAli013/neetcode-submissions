class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myd = {}
        for s in strs:
            ns = sorted(s)
            ns = ''.join(ns) # cat => act
            if ns not in myd:
                myd[ns]=[]
            myd[ns].append(s)
        return list(myd.values())
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            cut = s2[i:i+len(s1)]
            cut = sorted(cut)
            if s1 == cut:
                return True
        return False

        
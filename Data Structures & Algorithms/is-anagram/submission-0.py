class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        s_freq = {}
        for i_s in s_list:
            s_freq[i_s] = s_freq.get(i_s,0)+1
        t_freq = {}
        for i_t in t_list:
            t_freq[i_t] = t_freq.get(i_t,0)+1
        if s_freq == t_freq:
            return True
        else:
            return False
        
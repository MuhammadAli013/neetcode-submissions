class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s == '': return 0
        # string = s
        # highest_number = 1
        # for L_id in range(len(string)):
        #     tmp_set = set()
        #     tmp_highest_num = 0
        #     for R_id in range(L_id,len(string)):
        #         char = string[R_id]
        #         if char not in tmp_set:
        #             tmp_set.add(char)
        #             tmp_highest_num += 1
        #         else:
        #             break
        #     highest_number = max(highest_number,tmp_highest_num)
        # return highest_number
        max_value = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l +1 
            charSet.add(s[r])
            max_value = max(max_value, r-l+1)
        return max_value
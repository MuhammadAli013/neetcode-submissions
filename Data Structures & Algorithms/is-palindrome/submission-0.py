class Solution:
    def isPalindrome(self, s: str) -> bool:
        input_str = s.lower()
        input_str = [ch for ch in input_str if ch.isalnum()]
        N = len(input_str)
        Palindrome = True
        for i in range(N):
            forward = i
            backward = N-i-1
            # print(forward,backward)
            if input_str[forward] == input_str[backward]:
                pass
            else:
                Palindrome = False
        return Palindrome
        
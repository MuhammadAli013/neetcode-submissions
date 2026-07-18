class Solution:
    def isValid(self, s: str) -> bool:
        input_str = s
        temp = []
        opening = ['(','[','{']
        closing = [')','}',']']
        dict = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        for ch in input_str:
            if ch in opening:
                temp.append(ch)
                print('open ', temp)
            elif ch in closing:
                if len(temp) == 0:
                    return False
                last_bracket = temp.pop()
                if not last_bracket == dict[ch]:
                    return False
        if len(temp) == 0:
            return True
        else: return False
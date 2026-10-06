class Solution:
    def isValid(self, s: str) -> bool:
        dict_s = {'(':')','{':'}','[':']'}
        stack_s = []
        for x in s:
            if x in dict_s.keys():
                stack_s.append(x)
            if x in dict_s.values():
                if len(stack_s)==0:
                    return False
                y = stack_s.pop()
                if dict_s[y]!=x:
                    return False
        if len(stack_s)!=0:
            return False
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # formatted_str = "".join([c for c in s if c.isalnum()])
        # left = 0
        # n = len(formatted_str)
        # right = n-1
        # while left<=right:
        #     if formatted_str[left].lower()!=formatted_str[right].lower():
        #         return False
        #     left+=1
        #     right-=1

        # return True
        l = 0
        n = len(s)
        r = n-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
        
        
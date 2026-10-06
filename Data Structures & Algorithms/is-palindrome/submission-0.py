class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str = "".join([c for c in s if c.isalnum()])
        left = 0
        n = len(formatted_str)
        right = n-1
        while left<=right:
            if formatted_str[left].lower()!=formatted_str[right].lower():
                return False
            left+=1
            right-=1

        return True
        
        
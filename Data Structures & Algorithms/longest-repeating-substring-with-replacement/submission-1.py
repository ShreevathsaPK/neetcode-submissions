class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l = 0
        r = 0
        n = len(s)
        dictionary = {chr(i):0 for i in range(ord('A'),ord('Z')+1)}
        while(r<n):
            dictionary[s[r]]+=1
            while (r-l+1) - max(dictionary.values()) >k:
                dictionary[s[l]]-=1
                l+=1
            
            max_length = max(max_length,(r-l+1))                
            r +=1
        return max_length
            
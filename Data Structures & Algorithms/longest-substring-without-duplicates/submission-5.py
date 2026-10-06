class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)
        r=0
        l=0
        dictionary = {}
        while(r<n):
            if s[r] not in dictionary:
                dictionary[s[r]]=1
            else :         
                dictionary[s[r]]+=1
            if dictionary[s[r]]>1:
                while(dictionary[s[r]]!=1) and l<r:                    
                    dictionary[s[l]]-=1
                    l+=1
            # length = (r-l+1)
            max_length = max((r-l+1),max_length)
            r+=1

        return max_length

            
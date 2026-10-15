class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = dict(Counter(t))
        l=0
        r=0
        need = len(t_dict)
        n=len(s)
        min_substr = ""
        min_len = float("inf")
        temp_dict = {}
        have = 0
        while(r<n):
            if s[r] in t_dict:
                if s[r] not in temp_dict:
                    temp_dict[s[r]]=1
                else:
                    temp_dict[s[r]]+=1
                if temp_dict[s[r]] == t_dict[s[r]]:
                    have += 1
            while have==need:
                #min_substr = s[l:r+1]
                _len = r-l+1
                if _len<min_len:
                    min_substr = s[l:r+1]
                    min_len = _len
                if s[l] in t_dict:
                    if temp_dict[s[l]] == t_dict[s[l]]:
                        have -=1
                    temp_dict[s[l]]-=1
                l+=1
            
            r+=1

        return min_substr
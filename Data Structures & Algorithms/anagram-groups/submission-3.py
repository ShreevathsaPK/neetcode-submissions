class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorts = ''.join(sorted(s))
            if sorts not in res:
                res[sorts] = []
            res[sorts].append(s)
        return [values for values in res.values()]
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictya = Counter(s)
        dictyb = Counter(t)
        if dictya == dictyb:
            return True
        else:
            return False
        
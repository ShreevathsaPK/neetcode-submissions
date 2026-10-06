class Solution:

    def encode(self, strs: List[str]) -> str:
        trans=""
        for x in strs:
            trans=trans+"₹"+x
        return trans

 

    def decode(self, s: str) -> List[str]:
        strs=s.split("₹")
        return strs[1:]

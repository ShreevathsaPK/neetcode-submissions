class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(x))+"$" for x in strs])+"#"+"".join(strs)
 

    def decode(self, s: str) -> List[str]:
        controls, data = s.split("#", 1)
        controls_1 = controls.split("$")[:-1]

        strs_dec = []

        for n in controls_1:
            strs_dec.append(data[0:int(n)])
            data = data[int(n):]

        return strs_dec

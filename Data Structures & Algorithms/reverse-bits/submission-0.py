class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)
        chopped_bin_n = bin_n[2:].zfill(32)
        reversed_chopped_bin_n = chopped_bin_n[::-1]
        return int(reversed_chopped_bin_n,2)

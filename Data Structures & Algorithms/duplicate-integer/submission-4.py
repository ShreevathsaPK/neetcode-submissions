class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dicty = {}
        for x in nums:
            dicty[x] = dicty.get(x, 0) + 1
            if dicty[x]>=2:
                return True
        return False
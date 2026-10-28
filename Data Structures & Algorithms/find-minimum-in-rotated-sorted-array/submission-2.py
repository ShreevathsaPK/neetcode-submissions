class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums[0],nums[1])
        k = int(n/2)
        return min(Solution.findMin(self,nums[:k]),Solution.findMin(self,nums[k:]))
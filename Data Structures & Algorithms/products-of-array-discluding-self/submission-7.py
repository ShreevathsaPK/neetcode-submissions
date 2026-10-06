class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_new = [1] * n
        prefix= 1

        for i in range(n):
            nums_new[i] = prefix
            prefix = nums[i]*prefix
        suffix=1
        for i in range(n - 1, -1, -1):
            nums_new[i] = suffix*nums_new[i]
            suffix = nums[i]*suffix
        return nums_new




        
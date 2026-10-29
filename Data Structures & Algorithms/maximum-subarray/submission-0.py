class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_,sum = nums[0],0
        for num in nums:
            if sum<0:
                sum=0
            sum += num
            max_ = max(max_,sum)
        return max_
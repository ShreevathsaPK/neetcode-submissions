class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r=0,n-1
        while(l<r):
            k = l+(r-l)//2
            if nums[k]<nums[r]:
                r=k
            else:
                l=k+1
        return nums[l]
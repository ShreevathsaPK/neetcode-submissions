class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictya = {}
        for i in range(0,len(nums)):
            if nums[i] not in dictya:
                dictya[nums[i]]= i

        for j in range(len(nums)):
            if target-nums[j] in dictya and dictya[target-nums[j]] != j:
                return sorted([dictya[target-nums[j]],j])
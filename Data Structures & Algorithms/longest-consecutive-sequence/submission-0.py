class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest =0 
        for n in nums:
            if (n-1) not in numset:
                largest = 0
                while (n+largest) in numset:
                    largest+=1
                longest = max(largest,longest)
        return longest

        
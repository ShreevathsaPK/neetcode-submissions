class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0
        while(l<r):
            new_area = (r-l)*min(heights[l],heights[r])
            l,r = (l+1,r)  if heights[l]<heights[r] else (l,r-1)
            max_area = max(max_area,new_area)
        return max_area
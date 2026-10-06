class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            j=i+1
            k=n-1
            #[-4,-1,-1,0,1,2]
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]==0:
                    result.append(sorted([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1        
        #print(result)
        set_res = set(map(tuple,result))
        fin_res = [list(x) for x in set_res]
        return fin_res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for ele in nums:
            if ele not in res:
                res[ele]=1
            else:
                res[ele]+=1

        res2 = sorted(res.keys(),key=lambda x:res[x], reverse=True)[:k]
        return res2